# poll_tokens()

- **Type:** Function
- **File:** [`modules/poll/poll.tokens.inc`](_file.md), lines 41–107 · [local source](../../../../source/modules/poll/poll.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.tokens.inc#L41-L107)
- **Module/theme:** poll
- **Implements:** [hook_tokens()](../../system/system.api.php/hook_tokens.md)

## Signature

```php
function poll_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function poll_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $sanitize = !empty($options['sanitize']);
  if (isset($options['language'])) {
    $url_options['language'] = $options['language'];
    $language_code = $options['language']->language;
  }
  else {
    $language_code = NULL;
  }

  $replacements = array();

  if ($type == 'node' && !empty($data['node']) && $data['node']->type == 'poll') {
    $node = $data['node'];

    $total_votes = 0;
    $highest_votes = 0;
    foreach ($node->choice as $choice) {
      if ($choice['chvotes'] > $highest_votes) {
        $winner = $choice;
        $highest_votes = $choice['chvotes'];
      }
      $total_votes = $total_votes + $choice['chvotes'];
    }
    foreach ($tokens as $name => $original) {
      switch ($name) {
        case 'poll-votes':
          $replacements[$original] = $total_votes;
          break;

        case 'poll-winner':
          if (isset($winner)) {
            $replacements[$original] = $sanitize ? filter_xss($winner['chtext']) : $winner['chtext'];
          }
          else {
            $replacements[$original] = '';
          }
          break;

        case 'poll-winner-votes':
          if (isset($winner)) {
            $replacements[$original] = $winner['chvotes'];
          }
          else {
            $replacements[$original] = '';
          }
          break;

        case 'poll-winner-percent':
          if (isset($winner)) {
            $percent = ($winner['chvotes'] / $total_votes) * 100;
            $replacements[$original] = number_format($percent, 0);
          }
          else {
            $replacements[$original] = '';
          }
          break;

        case 'poll-duration':
          $replacements[$original] = format_interval($node->runtime, 1, $language_code);
          break;
      }
    }
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/poll/poll.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
