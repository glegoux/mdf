#!/bin/sh

message() {
    echo "${@}${NC}"
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
