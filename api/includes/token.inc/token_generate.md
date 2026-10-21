# token_generate()

- **Type:** Function
- **File:** [`includes/token.inc`](_file.md), lines 176–190 · [local source](../../../source/includes/token.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/token.inc#L176-L190)

## Signature

```php
function token_generate($type, array $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Generates replacement values for a list of tokens.

@param $type
  The type of token being replaced. 'node', 'user', and 'date' are common.
@param $tokens
  An array of tokens to be replaced, keyed by the literal text of the token
  as it appeared in the source text.
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
  - callback: A callback function that will be used to post-process the
    array of token replacements after they are generated. Can be used when
    modules require special formatting of token text, for example URL
    encoding or truncation to a specific length.
  - sanitize: A boolean flag indicating that tokens should be sanitized for
    display to a web browser. Developers who set this option to FALSE assume
    responsibility for running filter_xss(), check_plain() or other
    appropriate scrubbing functions before displaying data to users.

@return
  An associative array of replacement values, keyed by the original 'raw'
  tokens that were found in the source text. For example:
  $results['[node:title]'] = 'My new node';

@see hook_tokens()
@see hook_tokens_alter()
```

## Code

```php
function token_generate($type, array $tokens, array $data = array(), array $options = array()) {
  $options += array('sanitize' => TRUE);
  $replacements = module_invoke_all('tokens', $type, $tokens, $data, $options);

  // Allow other modules to alter the replacements.
  $context = array(
    'type' => $type,
    'tokens' => $tokens,
    'data' => $data,
    'options' => $options,
  );
  drupal_alter('tokens', $replacements, $context);

  return $replacements;
}
```

---
_Drupal 7.103 · [includes/token.inc](https://github.com/drupal/drupal/blob/7.103/includes/token.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
