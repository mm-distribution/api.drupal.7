# ContactPersonalTestCase::testPersonalContactAccess()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 329–409 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L329-L409)
- **Class:** [ContactPersonalTestCase](../ContactPersonalTestCase.md)
- **Module/theme:** contact

## Signature

```php
function testPersonalContactAccess()
```

## Documentation

```text
Tests access to the personal contact form.
```

## Code

```php
  function testPersonalContactAccess() {
    // Test allowed access to user with contact form enabled.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(200);

    // Test denied access to the user's own contact form.
    $this->drupalGet('user/' . $this->web_user->uid . '/contact');
    $this->assertResponse(403);

    // Test always denied access to the anonymous user contact form.
    $this->drupalGet('user/0/contact');
    $this->assertResponse(403);

    // Test that anonymous users can access the contact form.
    $this->drupalLogout();
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access user contact forms'));
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(200);

    // Test that users can disable their contact form.
    $this->drupalLogin($this->contact_user);
    $edit = array('contact' => FALSE);
    $this->drupalPost('user/' . $this->contact_user->uid . '/edit', $edit, 'Save');
    $this->drupalLogout();
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(403);

    // Test that user's contact status stays disabled when saving.
    $contact_user_temp = user_load($this->contact_user->uid, TRUE);
    user_save($contact_user_temp);
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(403);

    // Test that users can enable their contact form.
    $this->drupalLogin($this->contact_user);
    $edit = array('contact' => TRUE);
    $this->drupalPost('user/' . $this->contact_user->uid . '/edit', $edit, 'Save');
    $this->drupalLogout();
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(200);

    // Revoke the personal contact permission for the anonymous user.
    user_role_revoke_permissions(DRUPAL_ANONYMOUS_RID, array('access user contact forms'));
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(403);

    // Disable the personal contact form.
    $this->drupalLogin($this->admin_user);
    $edit = array('contact_default_status' => FALSE);
    $this->drupalPost('admin/config/people/accounts', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Setting successfully saved.');
    $this->drupalLogout();

    // Re-create our contacted user with personal contact forms disabled by
    // default.
    $this->contact_user = $this->drupalCreateUser();

    // Test denied access to a user with contact form disabled.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(403);

    // Test allowed access for admin user to a user with contact form disabled.
    $this->drupalLogin($this->admin_user);
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(200);

    // Re-create our contacted user as a blocked user.
    $this->contact_user = $this->drupalCreateUser();
    user_save($this->contact_user, array('status' => 0));

    // Test that blocked users can still be contacted by admin.
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(200);

    // Test that blocked users cannot be contacted by non-admins.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('user/' . $this->contact_user->uid . '/contact');
    $this->assertResponse(403);
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
