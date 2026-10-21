# poll_results()

- **Type:** Function
- **File:** [`modules/poll/poll.pages.inc`](_file.md), lines 93–97 · [local source](../../../../source/modules/poll/poll.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.pages.inc#L93-L97)
- **Module/theme:** poll

## Signature

```php
function poll_results($node)
```

## Documentation

```text
Callback for the 'results' tab for polls you can vote on
```

## Code

```php
function poll_results($node) {
  drupal_set_title($node->title);
  $node->show_results = TRUE;
  return node_show($node);
}
```

---
_Drupal 7.103 · [modules/poll/poll.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
