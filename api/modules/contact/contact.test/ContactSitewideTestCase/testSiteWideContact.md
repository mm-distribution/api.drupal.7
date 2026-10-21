# ContactSitewideTestCase::testSiteWideContact()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 26–161 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L26-L161)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
- **Module/theme:** contact

## Signature

```php
function testSiteWideContact()
```

## Documentation

```text
Tests configuration options and the site-wide contact form.
```

## Code

```php
  function testSiteWideContact() {
    // Create and login administrative user.
    $admin_user = $this->drupalCreateUser(array('access site-wide contact form', 'administer contact forms', 'administer users'));
    $this->drupalLogin($admin_user);

    $flood_limit = 3;
    variable_set('contact_threshold_limit', $flood_limit);
    variable_set('contact_threshold_window', 600);

    // Set settings.
    $edit = array();
    $edit['contact_default_status'] = TRUE;
    $this->drupalPost('admin/config/people/accounts', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Setting successfully saved.');

    // Delete old categories to ensure that new categories are used.
    $this->deleteCategories();

    // Ensure that the contact form won't be shown without categories.
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access site-wide contact form'));
    $this->drupalLogout();
    $this->drupalGet('contact');
    $this->assertResponse(404);
    $this->drupalLogin($admin_user);
    $this->drupalGet('contact');
    $this->assertResponse(200);
    $this->assertText(t('The contact form has not been configured.'));

    // Add categories.
    // Test invalid recipients.
    $invalid_recipients = array('invalid', 'invalid@', 'invalid@site.', '@site.', '@site.com');
    foreach ($invalid_recipients as $invalid_recipient) {
      $this->addCategory($this->randomName(16), $invalid_recipient, '', FALSE);
      $this->assertRaw(t('%recipient is an invalid e-mail address.', array('%recipient' => $invalid_recipient)), format_string('Caught invalid recipient (@invalid_recipient).', array('@invalid_recipient' => $invalid_recipient)));
    }

    // Test validation of empty category and recipients fields.
    $this->addCategory($category = '', '', '', TRUE);
    $this->assertText(t('Category field is required.'), 'Caught empty category field');
    $this->assertText(t('Recipients field is required.'), 'Caught empty recipients field.');

    // Create first valid category.
    $recipients = array('simpletest@example.com', 'simpletest2@example.com', 'simpletest3@example.com');
    $this->addCategory($category = $this->randomName(16), implode(',', array($recipients[0])), '', TRUE);
    $this->assertRaw(t('Category %category has been saved.', array('%category' => $category)), 'Category successfully saved.');

    // Make sure the newly created category is included in the list of categories.
    $this->assertNoUniqueText($category, 'New category included in categories list.');

    // Test update contact form category.
    $categories = $this->getCategories();
    $category_id = $this->updateCategory($categories, $category = $this->randomName(16), $recipients_str = implode(',', array($recipients[0], $recipients[1])), $reply = $this->randomName(30), FALSE);
    $category_array = db_query("SELECT category, recipients, reply, selected FROM {contact} WHERE cid = :cid", array(':cid' => $category_id))->fetchAssoc();
    $this->assertEqual($category_array['category'], $category);
    $this->assertEqual($category_array['recipients'], $recipients_str);
    $this->assertEqual($category_array['reply'], $reply);
    $this->assertFalse($category_array['selected']);
    $this->assertRaw(t('Category %category has been saved.', array('%category' => $category)), 'Category successfully saved.');

    // Ensure that the contact form is shown without a category selection input.
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access site-wide contact form'));
    $this->drupalLogout();
    $this->drupalGet('contact');
    $this->assertText(t('Your e-mail address'), 'Contact form is shown when there is one category.');
    $this->assertNoText(t('Category'), 'When there is only one category, the category selection element is hidden.');
    $this->drupalLogin($admin_user);

    // Add more categories.
    $this->addCategory($category = $this->randomName(16), implode(',', array($recipients[0], $recipients[1])), '', FALSE);
    $this->assertRaw(t('Category %category has been saved.', array('%category' => $category)), 'Category successfully saved.');

    $this->addCategory($category = $this->randomName(16), implode(',', array($recipients[0], $recipients[1], $recipients[2])), '', FALSE);
    $this->assertRaw(t('Category %category has been saved.', array('%category' => $category)), 'Category successfully saved.');

    // Try adding a category that already exists.
    $this->addCategory($category, '', '', FALSE);
    $this->assertNoRaw(t('Category %category has been saved.', array('%category' => $category)), 'Category not saved.');
    $this->assertRaw(t('A contact form with category %category already exists.', array('%category' => $category)), 'Duplicate category error found.');

    // Clear flood table in preparation for flood test and allow other checks to complete.
    db_delete('flood')->execute();
    $num_records_after = db_query("SELECT COUNT(*) FROM {flood}")->fetchField();
    $this->assertIdentical($num_records_after, '0', 'Flood table emptied.');
    $this->drupalLogout();

    // Check to see that anonymous user cannot see contact page without permission.
    user_role_revoke_permissions(DRUPAL_ANONYMOUS_RID, array('access site-wide contact form'));
    $this->drupalGet('contact');
    $this->assertResponse(403, 'Access denied to anonymous user without permission.');

    // Give anonymous user permission and see that page is viewable.
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access site-wide contact form'));
    $this->drupalGet('contact');
    $this->assertResponse(200, 'Access granted to anonymous user with permission.');

    // Submit contact form with invalid values.
    $this->submitContact('', $recipients[0], $this->randomName(16), $categories[0], $this->randomName(64));
    $this->assertText(t('Your name field is required.'), 'Name required.');

    $this->submitContact($this->randomName(16), '', $this->randomName(16), $categories[0], $this->randomName(64));
    $this->assertText(t('Your e-mail address field is required.'), 'E-mail required.');

    $this->submitContact($this->randomName(16), $invalid_recipients[0], $this->randomName(16), $categories[0], $this->randomName(64));
    $this->assertText(t('You must enter a valid e-mail address.'), 'Valid e-mail required.');

    $this->submitContact($this->randomName(16), $recipients[0], '', $categories[0], $this->randomName(64));
    $this->assertText(t('Subject field is required.'), 'Subject required.');

    $this->submitContact($this->randomName(16), $recipients[0], $this->randomName(16), $categories[0], '');
    $this->assertText(t('Message field is required.'), 'Message required.');

    // Test contact form with no default category selected.
    db_update('contact')
      ->fields(array('selected' => 0))
      ->execute();
    $this->drupalGet('contact');
    $this->assertRaw(t('- Please choose -'), 'Without selected categories the visitor is asked to chose a category.');

    // Submit contact form with invalid category id (cid 0).
    $this->submitContact($this->randomName(16), $recipients[0], $this->randomName(16), 0, '');
    $this->assertText(t('You must select a valid category.'), 'Valid category required.');

    // Submit contact form with correct values and check flood interval.
    for ($i = 0; $i < $flood_limit; $i++) {
      $this->submitContact($this->randomName(16), $recipients[0], $this->randomName(16), $categories[0], $this->randomName(64));
      $this->assertText(t('Your message has been sent.'), 'Message sent.');
    }
    // Submit contact form one over limit.
    $this->drupalGet('contact');
    $this->assertResponse(403, 'Access denied to anonymous user after reaching message treshold.');
    $this->assertRaw(t('You cannot send more than %number messages in @interval. Try again later.', array('%number' => variable_get('contact_threshold_limit', 3), '@interval' => format_interval(600))), 'Message threshold reached.');

    // Delete created categories.
    $this->drupalLogin($admin_user);
    $this->deleteCategories();
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
