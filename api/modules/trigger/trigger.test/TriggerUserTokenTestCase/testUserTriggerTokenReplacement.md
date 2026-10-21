# TriggerUserTokenTestCase::testUserTriggerTokenReplacement()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 447–480 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L447-L480)
- **Class:** [TriggerUserTokenTestCase](../TriggerUserTokenTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testUserTriggerTokenReplacement()
```

## Documentation

```text
Tests a variety of token replacements in actions.
```

## Code

```php
  function testUserTriggerTokenReplacement() {
    $test_user = $this->drupalCreateUser(array('administer actions', 'administer users', 'change own username', 'access user profiles'));
    $this->drupalLogin($test_user);

    $triggers = array('user_login', 'user_insert', 'user_update', 'user_delete', 'user_logout', 'user_view');
    foreach ($triggers as $trigger) {
      $this->assignSystemMessageAction($trigger);
      $this->assignSystemEmailAction($trigger);
    }

    $this->drupalLogout();
    $this->assertSystemEmailTokenReplacement('user_logout', $test_user);

    $this->drupalLogin($test_user);
    $this->assertSystemMessageAndEmailTokenReplacement('user_login', $test_user, 2);
    $this->assertSystemMessageAndEmailTokenReplacement('user_view', $test_user, 2);

    $this->drupalPost("user/{$test_user->uid}/edit", array('name' => $test_user->name . '_changed'), t('Save'));
    $test_user->name .= '_changed'; // Since we just changed it.
    $this->assertSystemMessageAndEmailTokenReplacement('user_update', $test_user, 2);

    $this->drupalGet('user');
    $this->assertSystemMessageAndEmailTokenReplacement('user_view', $test_user);

    $new_user = $this->drupalCreateUser(array('administer actions', 'administer users', 'cancel account', 'access administration pages'));
    $this->assertSystemEmailTokenReplacement('user_insert', $new_user);

    $this->drupalLogin($new_user);
    $user_to_delete = $this->drupalCreateUser(array('access content'));
    variable_set('user_cancel_method', 'user_cancel_delete');

    $this->drupalPost("user/{$user_to_delete->uid}/cancel", array(), t('Cancel account'));
    $this->assertSystemMessageAndEmailTokenReplacement('user_delete', $user_to_delete);
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
