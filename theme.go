package main

import "github.com/charmbracelet/lipgloss"

// Layout constants
const (
	containerWidth  = 80
	containerHeight = 22
)

// Welcome screen
var welcome = lipgloss.NewStyle().
	BorderStyle(lipgloss.NormalBorder()).
	Height(3).
	Width(60).
	PaddingTop(1).
	BorderForeground(lipgloss.Color("#3D4142")).
	Align(lipgloss.Center).
	Background(lipgloss.Color("#3D4152"))

var welcometext = lipgloss.NewStyle().
	Bold(true).
	Italic(true).
	Foreground(lipgloss.Color("#D6C6B4"))

// Main app
var mainbox = lipgloss.NewStyle().
	BorderStyle(lipgloss.NormalBorder()).
	Height(10).
	Width(50).
	Background(lipgloss.Color("#3D4152"))
