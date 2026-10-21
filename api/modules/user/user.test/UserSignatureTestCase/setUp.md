# UserSignatureTestCase::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2447–2466 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2447-L2466)
- **Class:** [UserSignatureTestCase](../UserSignatureTestCase.md)
- **Module/theme:** user

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('comment');

    // Enable user signatures.
    variable_set('user_signatures', 1);

    // Prefetch text formats.
    $this->full_html_format = filter_format_load('full_html');
    $this->plain_text_format = filter_format_load('plain_text');

    // Create regular and administrative users.
    $this->web_user = $this->drupalCreateUser(array());
    $admin_permissions = array('administer comments');
    foreach (filter_formats() as $format) {
      if ($permission = filter_permission_name($format)) {
        $admin_permissions[] = $permission;
      }
    }
    $this->admin_user = $this->drupalCreateUser($admin_permissions);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
