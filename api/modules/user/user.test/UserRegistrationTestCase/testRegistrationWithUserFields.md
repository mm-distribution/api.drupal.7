# UserRegistrationTestCase::testRegistrationWithUserFields()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 175–255 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L175-L255)
- **Class:** [UserRegistrationTestCase](../UserRegistrationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRegistrationWithUserFields()
```

## Documentation

```text
Tests Field API fields on user registration forms.
```

## Code

```php
  function testRegistrationWithUserFields() {
    // Create a field, and an instance on 'user' entity type.
    $field = array(
      'type' => 'test_field',
      'field_name' => 'test_user_field',
      'cardinality' => 1,
    );
    field_create_field($field);
    $instance = array(
      'field_name' => 'test_user_field',
      'entity_type' => 'user',
      'label' => 'Some user field',
      'bundle' => 'user',
      'required' => TRUE,
      'settings' => array('user_register_form' => FALSE),
    );
    field_create_instance($instance);

    // Check that the field does not appear on the registration form.
    $this->drupalGet('user/register');
    $this->assertNoText($instance['label'], 'The field does not appear on user registration form');

    // Have the field appear on the registration form.
    $instance['settings']['user_register_form'] = TRUE;
    field_update_instance($instance);
    $this->drupalGet('user/register');
    $this->assertText($instance['label'], 'The field appears on user registration form');

    // Check that validation errors are correctly reported.
    $edit = array();
    $edit['name'] = $name = $this->randomName();
    $edit['mail'] = $mail = $edit['name'] . '@example.com';
    // Missing input in required field.
    $edit['test_user_field[und][0][value]'] = '';
    $this->drupalPost(NULL, $edit, t('Create new account'));
    $this->assertRaw(t('@name field is required.', array('@name' => $instance['label'])), 'Field validation error was correctly reported.');
    // Invalid input.
    $edit['test_user_field[und][0][value]'] = '-1';
    $this->drupalPost(NULL, $edit, t('Create new account'));
    $this->assertRaw(t('%name does not accept the value -1.', array('%name' => $instance['label'])), 'Field validation error was correctly reported.');

    // Submit with valid data.
    $value = rand(1, 255);
    $edit['test_user_field[und][0][value]'] = $value;
    $this->drupalPost(NULL, $edit, t('Create new account'));
    // Check user fields.
    $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
    $new_user = reset($accounts);
    $this->assertEqual($new_user->test_user_field[LANGUAGE_NONE][0]['value'], $value, 'The field value was correctly saved.');

    // Check that the 'add more' button works.
    $field['cardinality'] = FIELD_CARDINALITY_UNLIMITED;
    field_update_field($field);
    foreach (array('js', 'nojs') as $js) {
      $this->drupalGet('user/register');
      // Add two inputs.
      $value = rand(1, 255);
      $edit = array();
      $edit['test_user_field[und][0][value]'] = $value;
      if ($js == 'js') {
        $this->drupalPostAJAX(NULL, $edit, 'test_user_field_add_more');
        $this->drupalPostAJAX(NULL, $edit, 'test_user_field_add_more');
      }
      else {
        $this->drupalPost(NULL, $edit, t('Add another item'));
        $this->drupalPost(NULL, $edit, t('Add another item'));
      }
      // Submit with three values.
      $edit['test_user_field[und][1][value]'] = $value + 1;
      $edit['test_user_field[und][2][value]'] = $value + 2;
      $edit['name'] = $name = $this->randomName();
      $edit['mail'] = $mail = $edit['name'] . '@example.com';
      $this->drupalPost(NULL, $edit, t('Create new account'));
      // Check user fields.
      $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
      $new_user = reset($accounts);
      $this->assertEqual($new_user->test_user_field[LANGUAGE_NONE][0]['value'], $value, format_string('@js : The field value was correclty saved.', array('@js' => $js)));
      $this->assertEqual($new_user->test_user_field[LANGUAGE_NONE][1]['value'], $value + 1, format_string('@js : The field value was correclty saved.', array('@js' => $js)));
      $this->assertEqual($new_user->test_user_field[LANGUAGE_NONE][2]['value'], $value + 2, format_string('@js : The field value was correclty saved.', array('@js' => $js)));
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
