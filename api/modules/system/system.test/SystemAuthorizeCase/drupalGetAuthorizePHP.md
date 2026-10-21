# SystemAuthorizeCase::drupalGetAuthorizePHP()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2992–2994 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2992-L2994)
- **Class:** [SystemAuthorizeCase](../SystemAuthorizeCase.md)
- **Module/theme:** system

## Signature

```php
function drupalGetAuthorizePHP($page_title = 'system-test-auth')
```

## Documentation

```text
Helper function to initialize authorize.php and load it via drupalGet().

Initializing authorize.php needs to happen in the child Drupal
installation, not the parent. So, we visit a menu callback provided by
system_test.module which calls system_authorized_init() to initialize the
$_SESSION inside the test site, not the framework site. This callback
redirects to authorize.php when it's done initializing.

@see system_authorized_init().
```

## Code

```php
  function drupalGetAuthorizePHP($page_title = 'system-test-auth') {
    $this->drupalGet('system-test/authorize-init/' . $page_title);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
