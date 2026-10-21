# node_ranking()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1759–1789 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1759-L1789)
- **Module/theme:** node
- **Implements:** [hook_ranking()](../node.api.php/hook_ranking.md)

## Signature

```php
function node_ranking()
```

## Documentation

```text
Implements hook_ranking().
```

## Code

```php
function node_ranking() {
  // Create the ranking array and add the basic ranking options.
  $ranking = array(
    'relevance' => array(
      'title' => t('Keyword relevance'),
      // Average relevance values hover around 0.15
      'score' => 'i.relevance',
    ),
    'sticky' => array(
      'title' => t('Content is sticky at top of lists'),
      // The sticky flag is either 0 or 1, which is automatically normalized.
      'score' => 'n.sticky',
    ),
    'promote' => array(
      'title' => t('Content is promoted to the front page'),
      // The promote flag is either 0 or 1, which is automatically normalized.
      'score' => 'n.promote',
    ),
  );

  // Add relevance based on creation or changed date.
  if ($node_cron_last = variable_get('node_cron_last', 0)) {
    $ranking['recent'] = array(
      'title' => t('Recently posted'),
      // Exponential decay with half-life of 6 months, starting at last indexed node
      'score' => 'POW(2.0, (GREATEST(n.created, n.changed) - :node_cron_last) * 6.43e-8)',
      'arguments' => array(':node_cron_last' => $node_cron_last),
    );
  }
  return $ranking;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
