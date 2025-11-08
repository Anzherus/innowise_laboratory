"""
Test suite for Hello World Color application.

This module contains comprehensive tests for all components
of the color printing application, ensuring code quality,
correctness, and proper error handling.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from typing import List, Dict, Any

# Add parent directory to Python path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import modules to test
from main import HelloWorldPrinter, ColorConfig, main
from colorama import Fore, Back, Style


class TestColorConfig:
    """
    Test cases for ColorConfig class.
    
    Verifies proper initialization and attribute handling
    for color configuration objects.
    """
    
    def test_initialization_with_all_parameters(self) -> None:
        """
        Test ColorConfig creation with foreground, background, and style.
        
        Ensures all parameters are correctly assigned to object attributes.
        """
        # Setup
        expected_foreground = Fore.RED
        expected_background = Back.YELLOW
        expected_style = Style.BRIGHT
        
        # Execution
        config = ColorConfig(
            foreground=expected_foreground,
            background=expected_background,
            style=expected_style
        )
        
        # Verification
        assert config.foreground == expected_foreground
        assert config.background == expected_background
        assert config.style == expected_style
    
    def test_initialization_with_only_foreground(self) -> None:
        """
        Test ColorConfig creation with only required foreground parameter.
        
        Verifies that optional parameters default to None when not provided.
        """
        # Setup
        expected_foreground = Fore.GREEN
        
        # Execution
        config = ColorConfig(foreground=expected_foreground)
        
        # Verification
        assert config.foreground == expected_foreground
        assert config.background is None
        assert config.style is None
    
    def test_initialization_with_foreground_and_background(self) -> None:
        """
        Test ColorConfig creation with foreground and background only.
        
        Ensures style remains None when not specified.
        """
        # Setup
        expected_foreground = Fore.BLUE
        expected_background = Back.CYAN
        
        # Execution
        config = ColorConfig(
            foreground=expected_foreground,
            background=expected_background
        )
        
        # Verification
        assert config.foreground == expected_foreground
        assert config.background == expected_background
        assert config.style is None
    
    @pytest.mark.parametrize("foreground,background,style", [
        (Fore.RED, None, None),
        (Fore.GREEN, Back.WHITE, None),
        (Fore.BLUE, None, Style.BRIGHT),
        (Fore.MAGENTA, Back.CYAN, Style.DIM),
    ])
    def test_initialization_parameter_combinations(
        self, 
        foreground: str, 
        background: str, 
        style: str
    ) -> None:
        """
        Parameterized test for various ColorConfig parameter combinations.
        
        Args:
            foreground: Text color from colorama.Fore
            background: Background color from colorama.Back
            style: Text style from colorama.Style
        """
        # Execution
        config = ColorConfig(
            foreground=foreground,
            background=background,
            style=style
        )
        
        # Verification
        assert config.foreground == foreground
        assert config.background == background
        assert config.style == style


class TestHelloWorldPrinter:
    """
    Test cases for HelloWorldPrinter class.
    
    Comprehensive tests for message setup, text formatting,
    and output functionality.
    """
    
    def test_initialization_creates_correct_number_of_messages(self) -> None:
        """
        Test that printer initializes with exactly 4 predefined messages.
        
        Ensures the message setup method works correctly during object creation.
        """
        # Execution
        printer = HelloWorldPrinter()
        
        # Verification
        assert len(printer._messages) == 4
        assert isinstance(printer._messages, list)
    
    def test_message_structure_and_content(self) -> None:
        """
        Test the structure and required fields of each message.
        
        Verifies that all messages have correct keys and non-empty text.
        """
        # Setup
        printer = HelloWorldPrinter()
        required_keys = {"text", "config"}
        
        # Execution & Verification
        for message in printer._messages:
            assert isinstance(message, dict)
            assert set(message.keys()) == required_keys
            assert isinstance(message["text"], str)
            assert len(message["text"]) > 0
            assert isinstance(message["config"], ColorConfig)
            assert "Hello World" in message["text"]
    
    def test_format_colored_text_with_all_attributes(self) -> None:
        """
        Test text formatting with foreground, background, and style.
        
        Verifies that all color codes are properly combined in the output.
        """
        # Setup
        printer = HelloWorldPrinter()
        test_text = "Test Message"
        config = ColorConfig(
            foreground=Fore.RED,
            background=Back.YELLOW,
            style=Style.BRIGHT
        )
        
        # Execution
        formatted_text = printer._format_colored_text(test_text, config)
        
        # Verification
        assert Style.BRIGHT in formatted_text
        assert Back.YELLOW in formatted_text
        assert Fore.RED in formatted_text
        assert test_text in formatted_text
        # Ensure text appears after all color codes
        assert formatted_text.endswith(test_text)
    
    def test_format_colored_text_with_only_foreground(self) -> None:
        """
        Test text formatting with only foreground color.
        
        Ensures formatting works correctly when optional parameters are None.
        """
        # Setup
        printer = HelloWorldPrinter()
        test_text = "Green Text"
        config = ColorConfig(foreground=Fore.GREEN)
        
        # Execution
        formatted_text = printer._format_colored_text(test_text, config)
        
        # Verification
        assert Fore.GREEN in formatted_text
        assert test_text in formatted_text
        assert Back.YELLOW not in formatted_text  # Should not contain unspecified background
        assert Style.BRIGHT not in formatted_text  # Should not contain unspecified style
    
    def test_format_colored_text_empty_string(self) -> None:
        """
        Test text formatting with empty input string.
        
        Verifies edge case handling for empty text input.
        """
        # Setup
        printer = HelloWorldPrinter()
        empty_text = ""
        config = ColorConfig(foreground=Fore.BLUE)
        
        # Execution
        formatted_text = printer._format_colored_text(empty_text, config)
        
        # Verification
        assert Fore.BLUE in formatted_text
        assert formatted_text == f"{Fore.BLUE}"  # Should only contain color code for empty text
    
    @patch('builtins.print')
    def test_print_all_messages_calls_print_correctly(self, mock_print: MagicMock) -> None:
        """
        Test that print_all_messages calls print function for each message.
        
        Verifies the correct number of print calls and that each call
        contains the expected "Hello World" text.
        
        Args:
            mock_print: Mock object for the print function
        """
        # Setup
        printer = HelloWorldPrinter()
        expected_call_count = 4
        
        # Execution
        printer.print_all_messages()
        
        # Verification
        assert mock_print.call_count == expected_call_count
        
        # Verify each printed message contains "Hello World"
        for call in mock_print.call_args_list:
            args, kwargs = call
            printed_text = args[0]
            assert "Hello World" in printed_text
            assert kwargs == {}  # No keyword arguments should be passed
    
    @patch('builtins.print')
    def test_print_all_messages_output_order(self, mock_print: MagicMock) -> None:
        """
        Test that messages are printed in the correct predefined order.
        
        Verifies the sequence of message printing matches setup order.
        
        Args:
            mock_print: Mock object for the print function
        """
        # Setup
        printer = HelloWorldPrinter()
        expected_messages = [message["text"] for message in printer._messages]
        
        # Execution
        printer.print_all_messages()
        
        # Verification
        actual_messages = [call[0][0] for call in mock_print.call_args_list]
        
        for expected, actual in zip(expected_messages, actual_messages):
            assert expected in actual


class TestMainFunction:
    """
    Test cases for the main function and application entry point.
    
    Ensures proper application flow and error handling.
    """
    
    @patch('main.HelloWorldPrinter')
    def test_main_creates_printer_and_calls_print_methods(
        self, 
        mock_printer_class: MagicMock
    ) -> None:
        """
        Test that main function properly initializes printer and prints messages.
        
        Verifies the complete application workflow from entry point to output.
        
        Args:
            mock_printer_class: Mock object for HelloWorldPrinter class
        """
        # Setup
        mock_printer_instance = MagicMock()
        mock_printer_class.return_value = mock_printer_instance
        
        # Execution
        main()
        
        # Verification
        mock_printer_class.assert_called_once()
        mock_printer_instance.print_all_messages.assert_called_once()
    
    @patch('main.HelloWorldPrinter')
    @patch('builtins.print')
    def test_main_function_integration(
        self, 
        mock_print: MagicMock, 
        mock_printer_class: MagicMock
    ) -> None:
        """
        Integration test for main function with real printer instance.
        
        Verifies that main function works correctly without mocks
        for the printer functionality.
        
        Args:
            mock_print: Mock object for print function
            mock_printer_class: Mock object for HelloWorldPrinter class
        """
        # Setup - use real printer but mock the print calls
        real_printer = HelloWorldPrinter()
        mock_printer_class.return_value = real_printer
        
        # Execution
        main()
        
        # Verification
        mock_printer_class.assert_called_once()
        assert mock_print.call_count == 4


class TestErrorHandling:
    """
    Test cases for error handling and edge cases.
    
    Ensures robustness and proper behavior in exceptional situations.
    """
    
    def test_color_config_with_none_foreground(self) -> None:
        """
        Test ColorConfig behavior with None foreground.
        
        Verifies that None foreground is handled gracefully.
        """
        # Execution
        config = ColorConfig(foreground=None)  # type: ignore
        
        # Verification
        assert config.foreground is None
        assert config.background is None
        assert config.style is None
    
    @patch('main.init')
    def test_printer_initializes_colorama(
        self, 
        mock_colorama_init: MagicMock
    ) -> None:
        """
        Test that HelloWorldPrinter initializes colorama on creation.
        
        Verifies integration with colorama library.
        
        Args:
            mock_colorama_init: Mock object for colorama.init
        """
        # Execution
        HelloWorldPrinter()
        
        # Verification
        mock_colorama_init.assert_called_once_with(autoreset=True)


def test_module_can_be_imported() -> None:
    """
    Test that the main module can be imported without errors.
    
    Basic smoke test to verify module integrity and dependencies.
    """
    # This test will fail during import if there are syntax errors
    # or missing dependencies
    from main import HelloWorldPrinter, ColorConfig, main
    assert HelloWorldPrinter is not None
    assert ColorConfig is not None
    assert main is not None


if __name__ == "__main__":
    """
    Allow direct execution of test module for debugging purposes.
    """
    pytest.main([__file__, "-v", "--cov=main", "--cov-report=term-missing"])