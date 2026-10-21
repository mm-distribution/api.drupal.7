# DBLogTestCase::doUser()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 260–339 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L260-L339)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function doUser()
```

## Documentation

```text
Generates and then verifies some user events.
```

## Code

```php
  private function doUser() {
    // Set user variables.
    $name = $this->randomName();
    $pass = user_password();
    // Add a user using the form to generate an add user event (which is not
    // triggered by drupalCreateUser).
    $edit = array();
    $edit['name'] = $name;
    $edit['mail'] = $name . '@example.com';
    $edit['pass[pass1]'] = $pass;
    $edit['pass[pass2]'] = $pass;
    $edit['status'] = 1;
    $this->drupalPost('admin/people/create', $edit, t('Create new account'));
    $this->assertResponse(200);
    // Retrieve the user object.
    $user = user_load_by_name($name);
    $this->assertTrue($user != NULL, format_string('User @name was loaded', array('@name' => $name)));
    // pass_raw property is needed by drupalLogin.
    $user->pass_raw = $pass;
    // Login user.
    $this->drupalLogin($user);
    // Logout user.
    $this->drupalLogout();
    // Fetch the row IDs in watchdog that relate to the user.
    $result = db_query('SELECT wid FROM {watchdog} WHERE uid = :uid', array(':uid' => $user->uid));
    foreach ($result as $row) {
      $ids[] = $row->wid;
    }
    $count_before = (isset($ids)) ? count($ids) : 0;
    $this->assertTrue($count_before > 0, format_string('DBLog contains @count records for @name', array('@count' => $count_before, '@name' => $user->name)));

    // Login the admin user.
    $this->drupalLogin($this->big_user);
    // Delete the user created at the start of this test.
    // We need to POST here to invoke batch_process() in the internal browser.
    $this->drupalPost('user/' . $user->uid . '/cancel', array('user_cancel_method' => 'user_cancel_reassign'), t('Cancel account'));

    // View the database log report.
    $this->drupalGet('admin/reports/dblog');
    $this->assertResponse(200);

    // Verify that the expected events were recorded.
    // Add user.
    // Default display includes name and email address; if too long, the email
    // address is replaced by three periods.
    $this->assertLogMessage(t('New user: %name (%email).', array('%name' => $name, '%email' => $user->mail)), 'DBLog event was recorded: [add user]');
    // Login user.
    $this->assertLogMessage(t('Session opened for %name.', array('%name' => $name)), 'DBLog event was recorded: [login user]');
    // Logout user.
    $this->assertLogMessage(t('Session closed for %name.', array('%name' => $name)), 'DBLog event was recorded: [logout user]');
    // Delete user.
    $message = t('Deleted user: %name %email.', array('%name' => $name, '%email' => '<' . $user->mail . '>'));
    $message_text = truncate_utf8(filter_xss($message, array()), 56, TRUE, TRUE);
    // Verify that the full message displays on the details page.
    $link = FALSE;
    if ($links = $this->xpath('//a[text()="' . html_entity_decode($message_text) . '"]')) {
      // Found link with the message text.
      $links = array_shift($links);
      foreach ($links->attributes() as $attr => $value) {
        if ($attr == 'href') {
          // Extract link to details page.
          $link = drupal_substr($value, strpos($value, 'admin/reports/event/'));
          $this->drupalGet($link);
          // Check for full message text on the details page.
          $this->assertRaw($message, 'DBLog event details was found: [delete user]');
          break;
        }
      }
    }
    $this->assertTrue($link, 'DBLog event was recorded: [delete user]');
    // Visit random URL (to generate page not found event).
    $not_found_url = $this->randomName(60);
    $this->drupalGet($not_found_url);
    $this->assertResponse(404);
    // View the database log page-not-found report page.
    $this->drupalGet('admin/reports/page-not-found');
    $this->assertResponse(200);
    // Check that full-length URL displayed.
    $this->assertText($not_found_url, 'DBLog event was recorded: [page not found]');
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
