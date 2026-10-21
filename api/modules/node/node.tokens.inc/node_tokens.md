# node_tokens()

- **Type:** Function
- **File:** [`modules/node/node.tokens.inc`](_file.md), lines 92–210 · [local source](../../../../source/modules/node/node.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.tokens.inc#L92-L210)
- **Module/theme:** node
- **Implements:** [hook_tokens()](../../system/system.api.php/hook_tokens.md)

## Signature

```php
function node_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function node_tokens($type, $tokens, array $data = array(), array $options = array()) {
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
          $replacements[$original] = isset($node->nid) ? $node->nid : '';
          break;

        case 'vid':
          $replacements[$original] = $node->vid;
          break;

        case 'tnid':
          $replacements[$original] = $node->tnid;
          break;

        case 'type':
          $replacements[$original] = $sanitize ? check_plain($node->type) : $node->type;
          break;

        case 'type-name':
          $type_name = node_type_get_name($node);
          $replacements[$original] = $sanitize ? check_plain($type_name) : $type_name;
          break;

        case 'title':
          $replacements[$original] = $sanitize ? check_plain($node->title) : $node->title;
          break;

        case 'body':
        case 'summary':
          if ($items = field_get_items('node', $node, 'body', $language_code)) {
            $instance = field_info_instance('node', 'body', $node->type);
            $field_langcode = field_language('node', $node, 'body', $language_code);
            // If the summary was requested and is not empty, use it.
            if ($name == 'summary' && !empty($items[0]['summary'])) {
              $output = $sanitize ? _text_sanitize($instance, $field_langcode, $items[0], 'summary') : $items[0]['summary'];
            }
            // Attempt to provide a suitable version of the 'body' field.
            else {
              $output = $sanitize ? _text_sanitize($instance, $field_langcode, $items[0], 'value') : $items[0]['value'];
              // A summary was requested.
              if ($name == 'summary') {
                if (isset($instance['display']['teaser']['settings']['trim_length'])) {
                  $trim_length = $instance['display']['teaser']['settings']['trim_length'];
                }
                else {
                  // Use default value.
                  $trim_length = NULL;
                }
                // Generate an optionally trimmed summary of the body field.
                $output = text_summary($output, $instance['settings']['text_processing'] ? $items[0]['format'] : NULL, $trim_length);
              }
            }
            $replacements[$original] = $output;
          }
          break;

        case 'language':
          $langcode = entity_language('node', $node);
          $replacements[$original] = $sanitize ? check_plain($langcode) : $langcode;
          break;

        case 'url':
          $replacements[$original] = isset($node->nid) ? url('node/' . $node->nid, $url_options) : '';
          break;

        case 'edit-url':
          $replacements[$original] = isset($node->nid) ? url('node/' . $node->nid . '/edit', $url_options) : '';
          break;

        // Default values for the chained tokens handled below.
        case 'author':
          $account = user_load($node->uid);
          $name = format_username($account);
          $replacements[$original] = $sanitize ? check_plain($name) : $name;
          break;

        case 'created':
          $replacements[$original] = format_date($node->created, 'medium', '', NULL, $language_code);
          break;

        case 'changed':
          $replacements[$original] = format_date($node->changed, 'medium', '', NULL, $language_code);
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

    if ($changed_tokens = token_find_with_prefix($tokens, 'changed')) {
      $replacements += token_generate('date', $changed_tokens, array('date' => $node->changed), $options);
    }
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/node/node.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
