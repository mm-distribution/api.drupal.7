# UserSignatureTestCase::testUserSignature()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2472–2516 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2472-L2516)
- **Class:** [UserSignatureTestCase](../UserSignatureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserSignature()
```

## Documentation

```text
Test that a user can change their signature format and that it is respected
upon display.
```

## Code

```php
  function testUserSignature() {
    // Create a new node with comments on.
    $node = $this->drupalCreateNode(array('comment' => COMMENT_NODE_OPEN));

    // Verify that user signature field is not displayed on registration form.
    $this->drupalGet('user/register');
    $this->assertNoText(t('Signature'));

    // Log in as a regular user and create a signature.
    $this->drupalLogin($this->web_user);
    $signature_text = "<h1>" . $this->randomName() . "</h1>";
    $edit = array(
      'signature[value]' => $signature_text,
      'signature[format]' => $this->plain_text_format->format,
    );
    $this->drupalPost('user/' . $this->web_user->uid . '/edit', $edit, t('Save'));

    // Verify that values were stored.
    $this->assertFieldByName('signature[value]', $edit['signature[value]'], 'Submitted signature text found.');
    $this->assertFieldByName('signature[format]', $edit['signature[format]'], 'Submitted signature format found.');

    // Create a comment.
    $langcode = LANGUAGE_NONE;
    $edit = array();
    $edit['subject'] = $this->randomName(8);
    $edit['comment_body[' . $langcode . '][0][value]'] = $this->randomName(16);
    $this->drupalPost('comment/reply/' . $node->nid, $edit, t('Preview'));
    $this->drupalPost(NULL, array(), t('Save'));

    // Get the comment ID. (This technique is the same one used in the Comment
    // module's CommentHelperCase test case.)
    preg_match('/#comment-([0-9]+)/', $this->getURL(), $match);
    $comment_id = $match[1];

    // Log in as an administrator and edit the comment to use Full HTML, so
    // that the comment text itself is not filtered at all.
    $this->drupalLogin($this->admin_user);
    $edit['comment_body[' . $langcode . '][0][format]'] = $this->full_html_format->format;
    $this->drupalPost('comment/' . $comment_id . '/edit', $edit, t('Save'));

    // Assert that the signature did not make it through unfiltered.
    $this->drupalGet('node/' . $node->nid);
    $this->assertNoRaw($signature_text, 'Unfiltered signature text not found.');
    $this->assertRaw(check_markup($signature_text, $this->plain_text_format->format), 'Filtered signature text found.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
