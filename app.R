library(shiny)
library(tidyverse)

immigration <- read_csv("immigration1 (2).csv")
family <- read_csv("immigrant_families2.csv")

immigrant_families <- immigration %>% 
  left_join(family, by ="family_record_num")

#for app
shiny_data <- immigrant_families %>% 
  select(vessel, age, sex, arrival_year) %>% 
  filter(!is.na(sex))

ui = fluidPage(
  sliderInput(inputId = "num",
              label = "Choose a year",
              value = 1844, min = 1844, max = 1850,
              sep = ""),
  plotOutput("galveston")
)

server <- function(input, output) {
  output$galveston <- renderPlot({
    shiny_data %>% 
      filter (arrival_year== input$num) %>% 
      ggplot(aes(x=age, fill = sex))+
      geom_bar(position = "stack") +
      theme_minimal()+ 
      scale_fill_brewer(palette = 2) +
      ggtitle("Galveston Immigrants by Age and Sex, 1844-1967")+
      xlab("Age")+
      ylab("Number of Immigrants") +
      scale_x_continuous(limits = c(0, 80))+
      scale_y_continuous(limits = c(0, 40))
  })
}


shinyApp(ui = ui, server = server)

