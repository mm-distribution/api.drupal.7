# poll_teaser()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 688–698 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L688-L698)
- **Module/theme:** poll

## Signature

```php
function poll_teaser($node)
```

## Documentation

```text
Creates a simple teaser that lists all the choices.

This is primarily used for RSS.
```

## Code

```php
function poll_teaser($node) {
  $teaser = NULL;
  if (is_array($node->choice)) {
    foreach ($node->choice as $choice) {
      if ($choice['chtext'] != '') {
        $teaser .= '* ' . check_plain($choice['chtext']) . "\n";
      }
    }
  }
  return $teaser;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
