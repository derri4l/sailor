package main

import (
	"time"

	tea "github.com/charmbracelet/bubbletea"
)

type model struct {
	phase string
}

type msgdone struct{}

func sail() model {
	return model{
		phase: "welcome",
	}
}

func (m model) Init() tea.Cmd {
	return tea.Tick(3*time.Second, func(t time.Time) tea.Msg {
		return msgdone{}
	})
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {

	case msgdone:
		m.phase = "main"
		return m, nil

	case tea.KeyMsg:
		if msg.String() == "esc" {
			return m, tea.Quit
		}
	}

	return m, nil
}

func (m model) View() string {

	if m.phase == "welcome" {
		title := welcometext.Render("S A I 𓊝  L O R")
		return welcome.Render(title)
	}

	return mainbox.Render("Main Screen")
}
