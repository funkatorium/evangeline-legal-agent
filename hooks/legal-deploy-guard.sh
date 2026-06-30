#!/usr/bin/env bash
# legal-deploy-guard.sh — Evangeline's Hook
# Detects legal content changes since the last deploy and forces
# acknowledgment before the deploy can proceed.
#
# ADHD-proof: this gate CANNOT be skipped. If legal content changed,
# you must confirm that customer notification was sent (or that there
# are zero customers to notify).
#
# Usage: Source this script in your deploy.sh, or call it directly:
#
#   # Option 1: Source it (recommended)
#   source hooks/legal-deploy-guard.sh
#   legal_deploy_guard "$DEPLOY_DIR" "$TAG_PREFIX"
#
#   # Option 2: Run standalone
#   ./hooks/legal-deploy-guard.sh _deploy deploy-prod
#
# Arguments:
#   $1 — deploy directory (default: _deploy)
#   $2 — tag prefix for finding last deploy (default: deploy-prod)
#
# Exit codes:
#   0 — no legal changes, or user confirmed
#   1 — user aborted (legal changes need notification first)
#
# Requirements:
#   - Git repo with deploy tags (e.g., deploy-prod-20260628-1430)
#   - Your legal content lives in the deploy directory
#
# What it detects:
#   AGB, Datenschutz, Widerrufsbelehrung, Impressum, Terms of Service,
#   Privacy Policy, Withdrawal notices — in German and English.
#
# German law context:
#   Under BGB and DSGVO, material changes to AGB or Datenschutz
#   require customer notification with reasonable notice (typically
#   30 days for AGB, "without undue delay" for DSGVO Art. 13/14).
#   This hook ensures you don't accidentally deploy legal changes
#   without sending that notification.
#
# Part of Evangeline — Legal Counsel Agent
# https://github.com/falcoschaefer99-eng/evangeline-legal-agent
# Apache 2.0

set -euo pipefail

legal_deploy_guard() {
  local DEPLOY_DIR="${1:-_deploy}"
  local TAG_PREFIX="${2:-deploy-prod}"

  # Find the last deploy tag
  local LAST_DEPLOY_TAG
  LAST_DEPLOY_TAG=$(git tag --list "${TAG_PREFIX}-*" --sort=-creatordate | head -1)
  local LEGAL_BASE="${LAST_DEPLOY_TAG:-HEAD~1}"

  # Check for legal content changes
  local LEGAL_CHANGED
  LEGAL_CHANGED=$(git diff "$LEGAL_BASE" -- "${DEPLOY_DIR}/" 2>/dev/null \
    | grep -iE '(Geschäftsbedingungen|Widerrufsbelehrung|Datenschutz|Widerrufsrecht|AGB|Terms of Service|Privacy Policy|Withdrawal|Impressum|Allgemeine Geschäftsbedingungen|Datenschutzerklärung)' \
    | grep -E '^\+' | head -5 || true)

  if [[ -z "$LEGAL_CHANGED" ]]; then
    return 0
  fi

  echo ""
  echo "╔══════════════════════════════════════════════════════════════════╗"
  echo "║  ⚖️  LEGAL CONTENT CHANGED — EVANGELINE'S HOOK                  ║"
  echo "╠══════════════════════════════════════════════════════════════════╣"
  echo "║  Changes detected in: AGB / Datenschutz / Widerrufsbelehrung   ║"
  echo "║                                                                ║"
  echo "║  German law requires you to notify existing customers of       ║"
  echo "║  material changes to terms and privacy policy.                 ║"
  echo "║                                                                ║"
  echo "║  Options:                                                      ║"
  echo "║    [n] I have notified all customers                           ║"
  echo "║    [z] I have zero paying customers to notify                  ║"
  echo "║    [f] This is the FIRST deploy of these legal pages           ║"
  echo "║    [q] Abort deploy — I need to send notifications first       ║"
  echo "╚══════════════════════════════════════════════════════════════════╝"
  echo ""
  read -rp "  Confirm [n/z/f/q]: " LEGAL_ACK
  case "$LEGAL_ACK" in
    n|N) echo "[deploy] ✓ Customer notification confirmed." ;;
    z|Z) echo "[deploy] ✓ Zero customers — no notification needed." ;;
    f|F) echo "[deploy] ✓ First deploy of legal pages — no prior version to notify about." ;;
    *)   echo "[deploy] ✗ Deploy aborted. Send notifications first."; exit 1 ;;
  esac
  echo ""
}

# If called directly (not sourced), run the function with CLI args
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  legal_deploy_guard "$@"
fi
