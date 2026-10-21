# OptionsWidgetsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 22–80 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L22-L80)
- **Class:** [OptionsWidgetsTestCase](../OptionsWidgetsTestCase.md)
- **Module/theme:** options

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('field_test', 'list_test');

    // Field with cardinality 1.
    $this->card_1 = array(
      'field_name' => 'card_1',
      'type' => 'list_integer',
      'cardinality' => 1,
      'settings' => array(
        'allowed_values' => array(
          // Make sure that 0 works as an option.
          0 => 'Zero',
          1 => 'One',
          // Make sure that option text is properly sanitized.
          2 => 'Some <script>dangerous</script> & unescaped <strong>markup</strong>',
          // Make sure that HTML entities in option text are not double-encoded.
          3 => 'Some HTML encoded markup with &lt; &amp; &gt;',
        ),
      ),
    );
    $this->card_1 = field_create_field($this->card_1);

    // Field with cardinality 2.
    $this->card_2 = array(
      'field_name' => 'card_2',
      'type' => 'list_integer',
      'cardinality' => 2,
      'settings' => array(
        'allowed_values' => array(
          // Make sure that 0 works as an option.
          0 => 'Zero',
          1 => 'One',
          // Make sure that option text is properly sanitized.
          2 => 'Some <script>dangerous</script> & unescaped <strong>markup</strong>',
        ),
      ),
    );
    $this->card_2 = field_create_field($this->card_2);

    // Boolean field.
    $this->bool = array(
      'field_name' => 'bool',
      'type' => 'list_boolean',
      'cardinality' => 1,
      'settings' => array(
        'allowed_values' => array(
          // Make sure that 1 works as a 'on' value'.
          1 => 'Zero',
          // Make sure that option text is properly sanitized.
          0 => 'Some <script>dangerous</script> & unescaped <strong>markup</strong>',
        ),
      ),
    );
    $this->bool = field_create_field($this->bool);

    // Create a web user.
    $this->web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content', 'administer fields'));
    $this->drupalLogin($this->web_user);
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
