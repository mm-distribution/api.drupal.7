# FieldFormTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1634–1661 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1634-L1661)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('field_test');

    $web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content'));
    $this->drupalLogin($web_user);

    $this->field_single = array('field_name' => 'field_single', 'type' => 'test_field');
    $this->field_multiple = array('field_name' => 'field_multiple', 'type' => 'test_field', 'cardinality' => 4);
    $this->field_unlimited = array('field_name' => 'field_unlimited', 'type' => 'test_field', 'cardinality' => FIELD_CARDINALITY_UNLIMITED);

    $this->instance = array(
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'label' => $this->randomName() . '_label',
      'description' => $this->randomName() . '_description',
      'weight' => mt_rand(0, 127),
      'settings' => array(
        'test_instance_setting' => $this->randomName(),
      ),
      'widget' => array(
        'type' => 'test_field_widget',
        'label' => 'Test Field',
        'settings' => array(
          'test_widget_setting' => $this->randomName(),
        )
      )
    );
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
