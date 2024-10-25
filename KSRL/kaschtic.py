import pygame
from langchain_ollama import OllamaLLM
import sys
model = OllamaLLM(model="llama3")



import re
def some_function():
    return" 

def ehp(func):
    pygame.init()

    window_width = 1000
    window_height = 600
    window_size = (window_width, window_height)

    # Create the window
    window = pygame.display.set_mode(window_size)
    
    # Create fonts
    fontc = pygame.font.SysFont(None, 48)  # Size 48 for main title
    font2 = pygame.font.SysFont(None, 22)  # Size 22 for error output
    font3 = pygame.font.SysFont(None, 22)  # Size 22 for "How to fix?" text

    # Set the title
    pygame.display.set_caption("Error Help Program (ehp)")

    white = (255, 255, 255)
    black = (0, 0, 0)

    # Render texts
    title_text = fontc.render('Error Program Help', True, black)
    output_text = font2.render('output(error)>>', True, black)

    # Initialize error text
    error_text = ""
    how_to_fix_surfaces = []  # List for rendering the solution
    fix_text = font3.render('How to fix?', True, black)  # Text for how to fix
    
    # Error handling
    try:
        func()  # Try to execute the passed function
    except Exception as e:
        error_text = f"Error: {str(e)}"  # Store the error message

        # Check if model is available for getting the solution
        if 'model' in globals():
            how_to_fix_text = model.invoke(f"Show me the solution for this error: {e}, please short and defined")
        else:
            how_to_fix_text = "No solution model available."

        # Clean up the text by removing unwanted characters
        how_to_fix_text = re.sub(r'[`*]', '', how_to_fix_text)  # Remove ` and *
        how_to_fix_text = re.sub(r'\s+', ' ', how_to_fix_text)  # Replace multiple spaces with a single space

        # Split the solution text into manageable lines
        words = how_to_fix_text.split(' ')
        current_line = ""
        for word in words:
            # Add word to the current line if it fits, otherwise start a new line
            if font3.size(current_line + word)[0] < window_width - 20:
                current_line += word + " "
            else:
                # Render the current line and reset it
                how_to_fix_surfaces.append(font3.render(current_line.strip(), True, black))
                current_line = word + " "
        # Render any remaining text in the current line
        if current_line:
            how_to_fix_surfaces.append(font3.render(current_line.strip(), True, black))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the window with white color
        window.fill(white)

        # Display the main title centered
        window.blit(title_text, (window_width // 2 - title_text.get_width() // 2, 50))
        
        # Display the output text 30 pixels below the title
        window.blit(output_text, (10, 50 + title_text.get_height() + 30))

        # Display the error text if there is an error
        if error_text:
            error_surface = font2.render(error_text, True, black)
            window.blit(error_surface, (10, 50 + title_text.get_height() + 70))  # 40 pixels below the output text
            
            # Display "How to fix?" text below the error message
            window.blit(fix_text, (10, 50 + title_text.get_height() + 100))
            
            # Display the solution lines with proper spacing
            y_position = 50 + title_text.get_height() + 130
            for surface in how_to_fix_surfaces:
                window.blit(surface, (10, y_position))
                y_position += 30  # Move down by 30 pixels for each line

        # Update the window
        pygame.display.update()

    # Quit pygame
    pygame.quit()
    sys.exit()
ehp(some_function)