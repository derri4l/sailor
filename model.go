// defines bubbletea model
package main

import tea "github.com/charmbracelet/bubbletea"

type model struct{}

func sail() model {
	return model{}
}

// init
func (m model) Init() tea.Cmd {
	return nil
}

// update
func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	return m, nil
}

// view
func (m model) View() string {
	return welcome.Render("Sailor")
}
