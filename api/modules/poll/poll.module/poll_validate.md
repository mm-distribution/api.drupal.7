# poll_validate()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 454–471 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L454-L471)
- **Module/theme:** poll
- **Implements:** [hook_validate()](../../node/node.api.php/hook_validate.md)

## Signature

```php
function poll_validate($node, $form)
```

## Documentation

```text
Implements hook_validate().
```

## Code

```php
function poll_validate($node, $form) {
  if (isset($node->title)) {
    // Check for at least two options and validate amount of votes.
    $realchoices = 0;
    foreach ($node->choice as $i => $choice) {
      if ($choice['chtext'] != '') {
        $realchoices++;
      }
      if (isset($choice['chvotes']) && $choice['chvotes'] < 0) {
        form_set_error("choice][$i][chvotes", t('Negative values are not allowed.'));
      }
    }

    if ($realchoices < 2) {
      form_set_error("choice][$realchoices][chtext", t('You must fill in at least two choices.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
