# hook_tokens()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4425–4479 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4425-L4479)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Provide replacement values for placeholder tokens.

This hook is invoked when someone calls token_replace(). That function first
scans the text for [type:token] patterns, and splits the needed tokens into
groups by type. Then hook_tokens() is invoked on each token-type group,
allowing your module to respond by providing replacement text for any of
the tokens in the group that your module knows how to process.

A module implementing this hook should also implement hook_token_info() in
order to list its available tokens on editing screens.

@param $type
  The machine-readable name of the type (group) of token being replaced, such
  as 'node', 'user', or another type defined by a hook_token_info()
  implementation.
@param $tokens
  An array of tokens to be replaced. The keys are the machine-readable token
  names, and the values are the raw [type:token] strings that appeared in the
  original text.
@param $data
  (optional) An associative array of data objects to be used when generating
  replacement values, as supplied in the $data parameter to token_replace().
@param $options
  (optional) An associative array of options for token replacement; see
  token_replace() for possible values.

@return
  An associative array of replacement values, keyed by the raw [type:token]
  strings from the original text.

@see hook_token_info()
@see hook_tokens_alter()
```

## Code

```php
function hook_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $url_options = array('absolute' => TRUE);
  if (isset($options['language'])) {
    $url_options['language'] = $options['language'];
    $language_code = $options['language']->language;
  }
  else {
    $language_code = NULL;
  }
  $sanitize = !empty($options['sanitize']);

  $replacements = array();

  if ($type == 'node' && !empty($data['node'])) {
    $node = $data['node'];

    foreach ($tokens as $name => $original) {
      switch ($name) {
        // Simple key values on the node.
        case 'nid':
          $replacements[$original] = $node->nid;
          break;

        case 'title':
          $replacements[$original] = $sanitize ? check_plain($node->title) : $node->title;
          break;

        case 'edit-url':
          $replacements[$original] = url('node/' . $node->nid . '/edit', $url_options);
          break;

        // Default values for the chained tokens handled below.
        case 'author':
          $name = ($node->uid == 0) ? variable_get('anonymous', t('Anonymous')) : $node->name;
          $replacements[$original] = $sanitize ? filter_xss($name) : $name;
          break;

        case 'created':
          $replacements[$original] = format_date($node->created, 'medium', '', NULL, $language_code);
          break;
      }
    }

    if ($author_tokens = token_find_with_prefix($tokens, 'author')) {
      $author = user_load($node->uid);
      $replacements += token_generate('user', $author_tokens, array('user' => $author), $options);
    }

    if ($created_tokens = token_find_with_prefix($tokens, 'created')) {
      $replacements += token_generate('date', $created_tokens, array('date' => $node->created), $options);
    }
  }

  return $replacements;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_tokens()".

- [comment_tokens()](../../comment/comment.tokens.inc/comment_tokens.md) — `modules/comment/comment.tokens.inc`
- [node_tokens()](../../node/node.tokens.inc/node_tokens.md) — `modules/node/node.tokens.inc`
- [poll_tokens()](../../poll/poll.tokens.inc/poll_tokens.md) — `modules/poll/poll.tokens.inc`
- [statistics_tokens()](../../statistics/statistics.tokens.inc/statistics_tokens.md) — `modules/statistics/statistics.tokens.inc`
- [system_tokens()](../system.tokens.inc/system_tokens.md) — `modules/system/system.tokens.inc`
- [taxonomy_tokens()](../../taxonomy/taxonomy.tokens.inc/taxonomy_tokens.md) — `modules/taxonomy/taxonomy.tokens.inc`
- [user_tokens()](../../user/user.tokens.inc/user_tokens.md) — `modules/user/user.tokens.inc`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
