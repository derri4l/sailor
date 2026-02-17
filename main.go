// boots everthing
package main

import tea "github.com/charmbracelet/bubbletea"

func main() {
	p := tea.NewProgram(sail())
	if err := p.Start(); err != nil {
		panic(err)
	}
}
