# poll_node_info()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 187–196 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L187-L196)
- **Module/theme:** poll
- **Implements:** [hook_node_info()](../../node/node.api.php/hook_node_info.md)

## Signature

```php
function poll_node_info()
```

## Documentation

```text
Implements hook_node_info().
```

## Code

```php
function poll_node_info() {
  return array(
    'poll' => array(
      'name' => t('Poll'),
      'base' => 'poll',
      'description' => t('A <em>poll</em> is a question with a set of possible responses. A <em>poll</em>, once created, automatically provides a simple running count of the number of votes received for each response.'),
      'title_label' => t('Question'),
    )
  );
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
