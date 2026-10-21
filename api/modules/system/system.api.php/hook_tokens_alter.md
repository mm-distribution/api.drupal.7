# hook_tokens_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4497–4519 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4497-L4519)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_tokens_alter(array &$replacements, array $context)
```

## Documentation

```text
Alter replacement values for placeholder tokens.

@param $replacements
  An associative array of replacements returned by hook_tokens().
@param $context
  The context in which hook_tokens() was called. An associative array with
  the following keys, which have the same meaning as the corresponding
  parameters of hook_tokens():
  - 'type'
  - 'tokens'
  - 'data'
  - 'options'

@see hook_tokens()
```

## Code

```php
function hook_tokens_alter(array &$replacements, array $context) {
  $options = $context['options'];

  if (isset($options['language'])) {
    $url_options['language'] = $options['language'];
    $language_code = $options['language']->language;
  }
  else {
    $language_code = NULL;
  }
  $sanitize = !empty($options['sanitize']);

  if ($context['type'] == 'node' && !empty($context['data']['node'])) {
    $node = $context['data']['node'];

    // Alter the [node:title] token, and replace it with the rendered content
    // of a field (field_title).
    if (isset($context['tokens']['title'])) {
      $title = field_view_field('node', $node, 'field_title', 'default', $language_code);
      $replacements[$context['tokens']['title']] = drupal_render($title);
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_tokens_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
