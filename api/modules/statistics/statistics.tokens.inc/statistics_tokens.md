# statistics_tokens()

- **Type:** Function
- **File:** [`modules/statistics/statistics.tokens.inc`](_file.md), lines 34–63 · [local source](../../../../source/modules/statistics/statistics.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.tokens.inc#L34-L63)
- **Module/theme:** statistics
- **Implements:** [hook_tokens()](../../system/system.api.php/hook_tokens.md)

## Signature

```php
function statistics_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function statistics_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $url_options = array('absolute' => TRUE);
  $replacements = array();

  if ($type == 'node' & !empty($data['node'])) {
    $node = $data['node'];

    foreach ($tokens as $name => $original) {
      if ($name == 'total-count') {
        $statistics = statistics_get($node->nid);
        $replacements[$original] = $statistics['totalcount'];
      }
      elseif ($name == 'day-count') {
        $statistics = statistics_get($node->nid);
        $replacements[$original] = $statistics['daycount'];
      }
      elseif ($name == 'last-view') {
        $statistics = statistics_get($node->nid);
        $replacements[$original] = format_date($statistics['timestamp']);
      }
    }

    if ($created_tokens = token_find_with_prefix($tokens, 'last-view')) {
      $statistics = statistics_get($node->nid);
      $replacements += token_generate('date', $created_tokens, array('date' => $statistics['timestamp']), $options);
    }
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
