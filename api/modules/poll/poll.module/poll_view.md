# poll_view()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 673–681 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L673-L681)
- **Module/theme:** poll
- **Implements:** [hook_view()](../../node/node.api.php/hook_view.md)

## Signature

```php
function poll_view($node, $view_mode)
```

## Documentation

```text
Implements hook_view().
```

## Code

```php
function poll_view($node, $view_mode) {
  if (!empty($node->allowvotes) && empty($node->show_results)) {
    $node->content['poll_view_voting'] = drupal_get_form('poll_view_voting', $node);
  }
  else {
    $node->content['poll_view_results'] = array('#markup' => poll_view_results($node, $view_mode));
  }
  return $node;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
