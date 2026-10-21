# token_replace()

- **Type:** Function
- **File:** [`includes/token.inc`](_file.md), lines 79–103 · [local source](../../../source/includes/token.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/token.inc#L79-L103)

## Signature

```php
function token_replace($text, array $data = array(), array $options = array())
```

## Documentation

```text
Replaces all tokens in a given string with appropriate values.

@param $text
  A string potentially containing replaceable tokens.
@param $data
  (optional) An array of keyed objects. For simple replacement scenarios
  'node', 'user', and others are common keys, with an accompanying node or
  user object being the value. Some token types, like 'site', do not require
  any explicit information from $data and can be replaced even if it is
  empty.
@param $options
  (optional) A keyed array of settings and flags to control the token
  replacement process. Supported options are:
  - language: A language object to be used when generating locale-sensitive
    tokens.
  - callback: A callback function that will be used to post-process the array
    of token replacements after they are generated. For example, a module
    using tokens in a text-only email might provide a callback to strip HTML
    entities from token values before they are inserted into the final text.
  - clear: A boolean flag indicating that tokens should be removed from the
    final text if no replacement value can be generated.
  - sanitize: A boolean flag indicating that tokens should be sanitized for
    display to a web browser. Defaults to TRUE. Developers who set this
    option to FALSE assume responsibility for running filter_xss(),
    check_plain() or other appropriate scrubbing functions before displaying
    data to users.

@return
  Text with tokens replaced.
```

## Code

```php
function token_replace($text, array $data = array(), array $options = array()) {
  $text_tokens = token_scan($text);
  if (empty($text_tokens)) {
    return $text;
  }

  $replacements = array();
  foreach ($text_tokens as $type => $tokens) {
    $replacements += token_generate($type, $tokens, $data, $options);
    if (!empty($options['clear'])) {
      $replacements += array_fill_keys($tokens, '');
    }
  }

  // Optionally alter the list of replacement values.
  if (!empty($options['callback']) && function_exists($options['callback'])) {
    $function = $options['callback'];
    $function($replacements, $data, $options);
  }

  $tokens = array_keys($replacements);
  $values = array_values($replacements);

  return str_replace($tokens, $values, $text);
}
```

---
_Drupal 7.103 · [includes/token.inc](https://github.com/drupal/drupal/blob/7.103/includes/token.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
