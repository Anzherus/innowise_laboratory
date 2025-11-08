"""
Hello World Color Printer

This module provides functionality to print colored "Hello World!" messages
to the terminal using the colorama library for cross-platform compatibility.
"""

from colorama import init, Fore, Back, Style
from typing import Dict, List, Optional


class ColorConfig:
    """Configuration class for color and style settings"""
    
    def __init__(self, foreground: str, background: Optional[str] = None, 
                 style: Optional[str] = None):
        """
        Initialize color configuration
        
        Args:
            foreground: Text color from colorama.Fore
            background: Background color from colorama.Back (optional)
            style: Text style from colorama.Style (optional)
        """
        self.foreground = foreground
        self.background = background
        self.style = style


class HelloWorldPrinter:
    """
    A class to handle printing colored Hello World messages.
    
    This class encapsulates all functionality related to generating
    and displaying colored terminal output.
    """
    
    def __init__(self):
        """Initialize the printer with colorama"""
        init(autoreset=True)
        self._messages = self._setup_messages()
    
    def _setup_messages(self) -> List[Dict[str, str]]:
        """
        Setup the collection of Hello World messages with their color configurations
        
        Returns:
            List of dictionaries containing text and color configuration
        """
        return [
            {
                "text": "Hello World!",
                "config": ColorConfig(Fore.RED, Back.YELLOW)
            },
            {
                "text": "Hello World in Green!",
                "config": ColorConfig(Fore.GREEN)
            },
            {
                "text": "Hello World in Bright Blue!",
                "config": ColorConfig(Fore.BLUE, style=Style.BRIGHT)
            },
            {
                "text": "Hello World with Magenta text and Cyan background!",
                "config": ColorConfig(Fore.MAGENTA, Back.CYAN)
            }
        ]
    
    def _format_colored_text(self, text: str, config: ColorConfig) -> str:
        """
        Format text with specified colors and styles
        
        Args:
            text: The text to format
            config: ColorConfig object with color and style settings
            
        Returns:
            Formatted string with color codes
        """
        color_parts = []
        
        # Add style if specified
        if config.style:
            color_parts.append(config.style)
        
        # Add background color if specified
        if config.background:
            color_parts.append(config.background)
        
        # Add foreground color
        color_parts.append(config.foreground)
        
        # Combine all parts with the text
        return f'{"".join(color_parts)}{text}'
    
    def print_all_messages(self) -> None:
        """
        Print all configured Hello World messages with their colors
        
        This is the main method that outputs all messages to stdout
        in the order they are configured.
        """
        for message in self._messages:
            formatted_text = self._format_colored_text(
                message["text"], 
                message["config"]
            )
            print(formatted_text)


def main() -> None:
    """
    Main execution function for the Hello World Color Printer
    
    This function demonstrates the usage of the HelloWorldPrinter class
    and handles the primary application workflow.
    """
    try:
        # Create printer instance
        printer = HelloWorldPrinter()
        
        # Display all colored messages
        printer.print_all_messages()
        
    except Exception as e:
        print(f"Error occurred: {e}")
        raise


if __name__ == "__main__":
    # Entry point of the application
    main()