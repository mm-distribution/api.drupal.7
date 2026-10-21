# TaxonomyThemeTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2018–2030 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2018-L2030)
- **Class:** [TaxonomyThemeTestCase](../TaxonomyThemeTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Make sure we are using distinct default and administrative themes for
    // the duration of these tests.
    variable_set('theme_default', 'bartik');
    variable_set('admin_theme', 'seven');

    // Create and log in as a user who has permission to add and edit taxonomy
    // terms and view the administrative theme.
    $admin_user = $this->drupalCreateUser(array('administer taxonomy', 'view the administration theme'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
