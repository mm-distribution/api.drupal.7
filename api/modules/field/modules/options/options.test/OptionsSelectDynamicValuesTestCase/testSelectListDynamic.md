# OptionsSelectDynamicValuesTestCase::testSelectListDynamic()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 561–579 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L561-L579)
- **Class:** [OptionsSelectDynamicValuesTestCase](../OptionsSelectDynamicValuesTestCase.md)
- **Module/theme:** options

## Signature

```php
function testSelectListDynamic()
```

## Documentation

```text
Tests the 'options_select' widget (single select).
```

## Code

```php
  function testSelectListDynamic() {
    // Create an entity.
    $this->entity->is_new = TRUE;
    field_test_entity_save($this->entity);
    // Create a web user.
    $web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content'));
    $this->drupalLogin($web_user);

    // Display form.
    $this->drupalGet('test-entity/manage/' . $this->entity->ftid . '/edit');
    $options = $this->xpath('//select[@id="edit-test-list-und"]/option');
    $this->assertEqual(count($options), count($this->test) + 1);
    foreach ($options as $option) {
      $value = (string) $option['value'];
      if ($value != '_none') {
        $this->assertTrue(array_search($value, $this->test));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
