# ShortcutTestCase::setUp()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 33–46 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L33-L46)
- **Class:** [ShortcutTestCase](../ShortcutTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('toolbar', 'shortcut');
    // Create users.
    $this->admin_user = $this->drupalCreateUser(array('access toolbar', 'administer shortcuts', 'view the administration theme', 'create article content', 'create page content', 'access content overview'));
    $this->shortcut_user = $this->drupalCreateUser(array('customize shortcut links', 'switch shortcut sets'));

    // Create a node.
    $this->node = $this->drupalCreateNode(array('type' => 'article'));

    // Log in as admin and grab the default shortcut set.
    $this->drupalLogin($this->admin_user);
    $this->set = shortcut_set_load(SHORTCUT_DEFAULT_SET_NAME);
    shortcut_set_assign_user($this->set, $this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
