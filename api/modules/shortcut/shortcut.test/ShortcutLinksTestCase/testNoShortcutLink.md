# ShortcutLinksTestCase::testNoShortcutLink()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 209–224 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L209-L224)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testNoShortcutLink()
```

## Documentation

```text
Tests that the add shortcut link is not displayed for 404/403 errors.

Tests that the "Add to shortcuts" link is not displayed on a page not
found or a page the user does not have access to.
```

## Code

```php
  function testNoShortcutLink() {
    // Change to a theme that displays shortcuts.
    variable_set('theme_default', 'seven');

    $this->drupalGet('page-that-does-not-exist');
    $this->assertNoRaw('add-shortcut', 'Add to shortcuts link was not shown on a page not found.');

    // The user does not have access to this path.
    $this->drupalGet('admin/modules');
    $this->assertNoRaw('add-shortcut', 'Add to shortcuts link was not shown on a page the user does not have access to.');

    // Verify that the testing mechanism works by verifying the shortcut
    // link appears on admin/content/node.
    $this->drupalGet('admin/content/node');
    $this->assertRaw('add-shortcut', 'Add to shortcuts link was shown on a page the user does have access to.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
