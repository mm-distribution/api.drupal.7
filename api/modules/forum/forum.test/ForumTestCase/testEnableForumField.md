# ForumTestCase::testEnableForumField()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 95–114 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L95-L114)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function testEnableForumField()
```

## Documentation

```text
Tests disabling and re-enabling the Forum module.
```

## Code

```php
  function testEnableForumField() {
    $this->drupalLogin($this->admin_user);

    // Disable the Forum module.
    $edit = array();
    $edit['modules[Core][forum][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    module_list(TRUE);
    $this->assertFalse(module_exists('forum'), 'Forum module is not enabled.');

    // Attempt to re-enable the Forum module and ensure it does not try to
    // recreate the taxonomy_forums field.
    $edit = array();
    $edit['modules[Core][forum][enable]'] = 'forum';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');
    module_list(TRUE);
    $this->assertTrue(module_exists('forum'), 'Forum module is enabled.');
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
