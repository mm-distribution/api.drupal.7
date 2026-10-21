# FilterAdminTestCase::testFormatAdmin()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 206–267 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L206-L267)
- **Class:** [FilterAdminTestCase](../FilterAdminTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFormatAdmin()
```

## Documentation

```text
Tests the format administration functionality.
```

## Code

```php
  function testFormatAdmin() {
    // Add text format.
    $this->drupalGet('admin/config/content/formats');
    $this->clickLink('Add text format');
    $format_id = drupal_strtolower($this->randomName());
    $name = $this->randomName();
    $edit = array(
      'format' => $format_id,
      'name' => $name,
    );
    $this->drupalPost(NULL, $edit, t('Save configuration'));

    // Verify default weight of the text format.
    $this->drupalGet('admin/config/content/formats');
    $this->assertFieldByName("formats[$format_id][weight]", 0, 'Text format weight was saved.');

    // Change the weight of the text format.
    $edit = array(
      "formats[$format_id][weight]" => 5,
    );
    $this->drupalPost('admin/config/content/formats', $edit, t('Save changes'));
    $this->assertFieldByName("formats[$format_id][weight]", 5, 'Text format weight was saved.');

    // Edit text format.
    $this->drupalGet('admin/config/content/formats');
    $this->assertLinkByHref('admin/config/content/formats/' . $format_id);
    $this->drupalGet('admin/config/content/formats/' . $format_id);
    $this->drupalPost(NULL, array(), t('Save configuration'));

    // Verify that the custom weight of the text format has been retained.
    $this->drupalGet('admin/config/content/formats');
    $this->assertFieldByName("formats[$format_id][weight]", 5, 'Text format weight was retained.');

    // Disable text format.
    $this->assertLinkByHref('admin/config/content/formats/' . $format_id . '/disable');
    $this->drupalGet('admin/config/content/formats/' . $format_id . '/disable');
    $this->drupalPost(NULL, array(), t('Disable'));

    // Verify that disabled text format no longer exists.
    $this->drupalGet('admin/config/content/formats/' . $format_id);
    $this->assertResponse(404, 'Disabled text format no longer exists.');

    // Attempt to create a format of the same machine name as the disabled
    // format but with a different human readable name.
    $edit = array(
      'format' => $format_id,
      'name' => 'New format',
    );
    $this->drupalPost('admin/config/content/formats/add', $edit, t('Save configuration'));
    $this->assertText('The machine-readable name is already in use. It must be unique.');

    // Attempt to create a format of the same human readable name as the
    // disabled format but with a different machine name.
    $edit = array(
      'format' => 'new_format',
      'name' => $name,
    );
    $this->drupalPost('admin/config/content/formats/add', $edit, t('Save configuration'));
    $this->assertRaw(t('Text format names must be unique. A format named %name already exists.', array(
      '%name' => $name,
    )));
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
