#!/bin/sh

# helper
message() {
    echo "${1}${2}${NC}"
}

error() {
    echo "${RED}ERROR: ${@}!${NC}"
}

success() {
    echo "${GREEN}SUCCESS: ${@}!${NC}"
}

info() {
    echo "${CYAN}${@}${NC}"
}
