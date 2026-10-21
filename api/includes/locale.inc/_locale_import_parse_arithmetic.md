# _locale_import_parse_arithmetic()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1286–1375 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1286-L1375)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_parse_arithmetic($string)
```

## Documentation

```text
Parses and sanitizes an arithmetic formula into a PHP expression

While parsing, we ensure, that the operators have the right
precedence and associativity.

@param $string
  A string containing the arithmetic formula.

@return
  The PHP version of the formula.
```

## Code

```php
function _locale_import_parse_arithmetic($string) {
  // Operator precedence table
  $precedence = array("(" => -1, ")" => -1, "?" => 1, ":" => 1, "||" => 3, "&&" => 4, "==" => 5, "!=" => 5, "<" => 6, ">" => 6, "<=" => 6, ">=" => 6, "+" => 7, "-" => 7, "*" => 8, "/" => 8, "%" => 8);
  // Right associativity
  $right_associativity = array("?" => 1, ":" => 1);

  $tokens = _locale_import_tokenize_formula($string);

  // Parse by converting into infix notation then back into postfix
  // Operator stack - holds math operators and symbols
  $operator_stack = array();
  // Element Stack - holds data to be operated on
  $element_stack = array();

  foreach ($tokens as $token) {
    $current_token = $token;

    // Numbers and the $n variable are simply pushed into $element_stack
    if (is_numeric($token)) {
      $element_stack[] = $current_token;
    }
    elseif ($current_token == "n") {
      $element_stack[] = '$n';
    }
    elseif ($current_token == "(") {
      $operator_stack[] = $current_token;
    }
    elseif ($current_token == ")") {
      $topop = array_pop($operator_stack);
      while (isset($topop) && ($topop != "(")) {
        $element_stack[] = $topop;
        $topop = array_pop($operator_stack);
      }
    }
    elseif (!empty($precedence[$current_token])) {
      // If it's an operator, then pop from $operator_stack into $element_stack until the
      // precedence in $operator_stack is less than current, then push into $operator_stack
      $topop = array_pop($operator_stack);
      while (isset($topop) && ($precedence[$topop] >= $precedence[$current_token]) && !(($precedence[$topop] == $precedence[$current_token]) && !empty($right_associativity[$topop]) && !empty($right_associativity[$current_token]))) {
        $element_stack[] = $topop;
        $topop = array_pop($operator_stack);
      }
      if ($topop) {
        $operator_stack[] = $topop;   // Return element to top
      }
      $operator_stack[] = $current_token;      // Parentheses are not needed
    }
    else {
      return FALSE;
    }
  }

  // Flush operator stack
  $topop = array_pop($operator_stack);
  while ($topop != NULL) {
    $element_stack[] = $topop;
    $topop = array_pop($operator_stack);
  }

  // Now extract formula from stack
  $previous_size = count($element_stack) + 1;
  while (count($element_stack) < $previous_size) {
    $previous_size = count($element_stack);
    for ($i = 2; $i < count($element_stack); $i++) {
      $op = $element_stack[$i];
      if (!empty($precedence[$op])) {
        $f = "";
        if ($op == ":") {
          $f = $element_stack[$i - 2] . "):" . $element_stack[$i - 1] . ")";
        }
        elseif ($op == "?") {
          $f = "(" . $element_stack[$i - 2] . "?(" . $element_stack[$i - 1];
        }
        else {
          $f = "(" . $element_stack[$i - 2] . $op . $element_stack[$i - 1] . ")";
        }
        array_splice($element_stack, $i - 2, 3, $f);
        break;
      }
    }
  }

  // If only one element is left, the number of operators is appropriate
  if (count($element_stack) == 1) {
    return $element_stack[0];
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
