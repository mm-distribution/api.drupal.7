# poll_block_info()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 133–137 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L133-L137)
- **Module/theme:** poll
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function poll_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function poll_block_info() {
  $blocks['recent']['info'] = t('Most recent poll');
  $blocks['recent']['properties']['administrative'] = TRUE;
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
