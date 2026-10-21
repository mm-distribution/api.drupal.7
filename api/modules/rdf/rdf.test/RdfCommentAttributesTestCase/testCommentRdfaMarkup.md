# RdfCommentAttributesTestCase::testCommentRdfaMarkup()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 480–526 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L480-L526)
- **Class:** [RdfCommentAttributesTestCase](../RdfCommentAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
public function testCommentRdfaMarkup()
```

## Documentation

```text
Tests the presence of the RDFa markup for the title, date and author and
homepage on registered users and anonymous comments.
```

## Code

```php
  public function testCommentRdfaMarkup() {

    // Posts comment #1 as a registered user.
    $this->drupalLogin($this->web_user);
    $comment1_subject = $this->randomName();
    $comment1_body = $this->randomName();
    $comment1 = $this->postComment($this->node1, $comment1_body, $comment1_subject);

    // Tests comment #1 with access to the user profile.
    $this->drupalGet('node/' . $this->node1->nid);
    $this->_testBasicCommentRdfaMarkup($comment1);

    // Tests comment #1 with no access to the user profile (as anonymous user).
    $this->drupalLogout();
    $this->drupalGet('node/' . $this->node1->nid);
    $this->_testBasicCommentRdfaMarkup($comment1);

    // Posts comment #2 as anonymous user.
    $comment2_subject = $this->randomName();
    $comment2_body = $this->randomName();
    $anonymous_user = array();
    $anonymous_user['name'] = $this->randomName();
    $anonymous_user['mail'] = 'tester@simpletest.org';
    $anonymous_user['homepage'] = 'http://example.org/';
    $comment2 = $this->postComment($this->node2, $comment2_body, $comment2_subject, $anonymous_user);
    $this->drupalGet('node/' . $this->node2->nid);

    // Tests comment #2 as anonymous user.
    $this->_testBasicCommentRdfaMarkup($comment2, $anonymous_user);
    // Tests the RDFa markup for the homepage (specific to anonymous comments).
    $comment_homepage = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//span[@rel="sioc:has_creator"]/a[contains(@class, "username") and @typeof="sioc:UserAccount" and @property="foaf:name" and @datatype="" and @href="http://example.org/" and contains(@rel, "foaf:page")]');
    $this->assertTrue(!empty($comment_homepage), 'RDFa markup for the homepage of anonymous user found.');
    // There should be no about attribute on anonymous comments.
    $comment_homepage = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//span[@rel="sioc:has_creator"]/a[@about]');
    $this->assertTrue(empty($comment_homepage), 'No about attribute is present on anonymous user comment.');

    // Tests comment #2 as logged in user.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node/' . $this->node2->nid);
    $this->_testBasicCommentRdfaMarkup($comment2, $anonymous_user);
    // Tests the RDFa markup for the homepage (specific to anonymous comments).
    $comment_homepage = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//span[@rel="sioc:has_creator"]/a[contains(@class, "username") and @typeof="sioc:UserAccount" and @property="foaf:name" and @datatype="" and @href="http://example.org/" and contains(@rel, "foaf:page")]');
    $this->assertTrue(!empty($comment_homepage), "RDFa markup for the homepage of anonymous user found.");
    // There should be no about attribute on anonymous comments.
    $comment_homepage = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//span[@rel="sioc:has_creator"]/a[@about]');
    $this->assertTrue(empty($comment_homepage), "No about attribute is present on anonymous user comment.");
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
