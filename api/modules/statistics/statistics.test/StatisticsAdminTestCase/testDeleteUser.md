# StatisticsAdminTestCase::testDeleteUser()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 404–426 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L404-L426)
- **Class:** [StatisticsAdminTestCase](../StatisticsAdminTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testDeleteUser()
```

## Documentation

```text
Tests that accesslog reflects when a user is deleted.
```

## Code

```php
  function testDeleteUser() {
    variable_set('statistics_enable_access_log', 1);

    variable_set('user_cancel_method', 'user_cancel_delete');
    $this->drupalLogout($this->privileged_user);
    $account = $this->drupalCreateUser(array('access content', 'cancel account'));
    $this->drupalLogin($account);
    $this->drupalGet('node/' . $this->test_node->nid);

    $account = user_load($account->uid, TRUE);

    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->drupalPost(NULL, NULL, t('Cancel account'));

    $timestamp = time();
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    // Confirm account cancellation request.
    $this->drupalGet("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail));
    $this->assertFalse(user_load($account->uid, TRUE), 'User is not found in the database.');

    $this->drupalGet('admin/reports/visitors');
    $this->assertNoText($account->name, 'Did not find user in visitor statistics.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
