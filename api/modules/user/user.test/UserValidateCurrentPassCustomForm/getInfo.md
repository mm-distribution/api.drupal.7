# UserValidateCurrentPassCustomForm::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2963–2969 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2963-L2969)
- **Class:** [UserValidateCurrentPassCustomForm](../UserValidateCurrentPassCustomForm.md)
- **Module/theme:** user

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'User validate current pass custom form',
      'description' => 'Test that user_validate_current_pass is usable on a custom form.',
      'group' => 'User',
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
