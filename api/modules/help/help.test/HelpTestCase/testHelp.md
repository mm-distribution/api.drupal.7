# HelpTestCase::testHelp()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 48–72 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L48-L72)
- **Class:** [HelpTestCase](../HelpTestCase.md)
- **Module/theme:** help

## Signature

```php
function testHelp()
```

## Documentation

```text
Logs in users, creates dblog events, and tests dblog functionality.
```

## Code

```php
  function testHelp() {
    // Login the admin user.
    $this->drupalLogin($this->big_user);
    $this->verifyHelp();

    // Login the regular user.
    $this->drupalLogin($this->any_user);
    $this->verifyHelp(403);

    // Check for css on admin/help.
    $this->drupalLogin($this->big_user);
    $this->drupalGet('admin/help');
    $this->assertRaw(drupal_get_path('module', 'help') . '/help.css', 'The help.css file is present in the HTML.');

    // Verify that introductory help text exists, goes for 100% module coverage.
    $this->assertRaw(t('For more information, refer to the specific topics listed in the next section or to the <a href="@drupal">online Drupal handbooks</a>.', array('@drupal' => 'http://drupal.org/documentation')), 'Help intro text correctly appears.');

    // Verify that help topics text appears.
    $this->assertRaw('<h2>' . t('Help topics') . '</h2><p>' . t('Help is available on the following items:') . '</p>', 'Help topics text correctly appears.');

    // Make sure links are properly added for modules implementing hook_help().
    foreach ($this->modules as $module => $name) {
      $this->assertLink($name, 0, format_string('Link properly added to @name (admin/help/@module)', array('@module' => $module, '@name' => $name)));
    }
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
