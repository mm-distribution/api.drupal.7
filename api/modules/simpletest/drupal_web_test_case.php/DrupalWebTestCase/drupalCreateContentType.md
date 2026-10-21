# DrupalWebTestCase::drupalCreateContentType()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1111–1150 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1111-L1150)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalCreateContentType($settings = array())
```

## Documentation

```text
Creates a custom content type based on default settings.

@param $settings
  An array of settings to change from the defaults.
  Example: 'type' => 'foo'.
@return
  Created content type.
```

## Code

```php
  protected function drupalCreateContentType($settings = array()) {
    // Find a non-existent random type name.
    do {
      $name = strtolower($this->randomName(8));
    } while (node_type_get_type($name));

    // Populate defaults array.
    $defaults = array(
      'type' => $name,
      'name' => $name,
      'base' => 'node_content',
      'description' => '',
      'help' => '',
      'title_label' => 'Title',
      'has_title' => 1,
    );
    // Imposed values for a custom type.
    $forced = array(
      'orig_type' => '',
      'old_type' => '',
      'module' => 'node',
      'custom' => 1,
      'modified' => 1,
      'locked' => 0,
    );
    $type = $forced + $settings + $defaults;
    $type = (object) $type;

    $saved_type = node_type_save($type);
    node_types_rebuild();
    menu_rebuild();
    node_add_body_field($type);

    $this->assertEqual($saved_type, SAVED_NEW, t('Created content type %type.', array('%type' => $type->type)));

    // Reset permissions so that permissions for this content type are available.
    $this->checkPermissions(array(), TRUE);

    return $type;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
