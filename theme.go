package main

import "github.com/charmbracelet/lipgloss"

// Layout constants
const (
	containerWidth  = 80
	containerHeight = 24
)

// Welcome screen
var welcome = lipgloss.NewStyle().
	BorderStyle(lipgloss.NormalBorder()).
	BorderForeground(lipgloss.Color(11))
