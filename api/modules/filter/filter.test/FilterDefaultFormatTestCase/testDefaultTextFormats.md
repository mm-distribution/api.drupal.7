# FilterDefaultFormatTestCase::testDefaultTextFormats()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 753–793 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L753-L793)
- **Class:** [FilterDefaultFormatTestCase](../FilterDefaultFormatTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testDefaultTextFormats()
```

## Documentation

```text
Tests if the default text format is accessible to users.
```

## Code

```php
  function testDefaultTextFormats() {
    // Create two text formats, and two users. The first user has access to
    // both formats, but the second user only has access to the second one.
    $admin_user = $this->drupalCreateUser(array('administer filters'));
    $this->drupalLogin($admin_user);
    $formats = array();
    for ($i = 0; $i < 2; $i++) {
      $edit = array(
        'format' => drupal_strtolower($this->randomName()),
        'name' => $this->randomName(),
      );
      $this->drupalPost('admin/config/content/formats/add', $edit, t('Save configuration'));
      $this->resetFilterCaches();
      $formats[] = filter_format_load($edit['format']);
    }
    list($first_format, $second_format) = $formats;
    $first_user = $this->drupalCreateUser(array(filter_permission_name($first_format), filter_permission_name($second_format)));
    $second_user = $this->drupalCreateUser(array(filter_permission_name($second_format)));

    // Adjust the weights so that the first and second formats (in that order)
    // are the two lowest weighted formats available to any user.
    $minimum_weight = db_query("SELECT MIN(weight) FROM {filter_format}")->fetchField();
    $edit = array();
    $edit['formats[' . $first_format->format . '][weight]'] = $minimum_weight - 2;
    $edit['formats[' . $second_format->format . '][weight]'] = $minimum_weight - 1;
    $this->drupalPost('admin/config/content/formats', $edit, t('Save changes'));
    $this->resetFilterCaches();

    // Check that each user's default format is the lowest weighted format that
    // the user has access to.
    $this->assertEqual(filter_default_format($first_user), $first_format->format, "The first user's default format is the lowest weighted format that the user has access to.");
    $this->assertEqual(filter_default_format($second_user), $second_format->format, "The second user's default format is the lowest weighted format that the user has access to, and is different than the first user's.");

    // Reorder the two formats, and check that both users now have the same
    // default.
    $edit = array();
    $edit['formats[' . $second_format->format . '][weight]'] = $minimum_weight - 3;
    $this->drupalPost('admin/config/content/formats', $edit, t('Save changes'));
    $this->resetFilterCaches();
    $this->assertEqual(filter_default_format($first_user), filter_default_format($second_user), 'After the formats are reordered, both users have the same default format.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
