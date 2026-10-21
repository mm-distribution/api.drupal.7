# RdfCommentAttributesTestCase::_testBasicCommentRdfaMarkup()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 564–577 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L564-L577)
- **Class:** [RdfCommentAttributesTestCase](../RdfCommentAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function _testBasicCommentRdfaMarkup($comment, $account = array())
```

## Documentation

```text
Helper function for testCommentRdfaMarkup().

Tests the current page for basic comment RDFa markup.

@param $comment
  Comment object.
@param $account
  An array containing information about an anonymous user.
```

## Code

```php
  function _testBasicCommentRdfaMarkup($comment, $account = array()) {
    $comment_container = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]');
    $this->assertTrue(!empty($comment_container), "Comment RDF type for comment found.");
    $comment_title = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//h3[@property="dc:title"]');
    $this->assertEqual((string)$comment_title[0]->a, $comment->subject, "RDFa markup for the comment title found.");
    $comment_date = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//*[contains(@property, "dc:date") and contains(@property, "dc:created")]');
    $this->assertTrue(!empty($comment_date), "RDFa markup for the date of the comment found.");
    // The author tag can be either a or span
    $comment_author = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//span[@rel="sioc:has_creator"]/*[contains(@class, "username") and @typeof="sioc:UserAccount" and @property="foaf:name" and @datatype=""]');
    $name = empty($account["name"]) ? $this->web_user->name : $account["name"] . " (not verified)";
    $this->assertEqual((string)$comment_author[0], $name, "RDFa markup for the comment author found.");
    $comment_body = $this->xpath('//div[contains(@class, "comment") and contains(@typeof, "sioct:Comment")]//div[@class="content"]//div[contains(@class, "comment-body")]//div[@property="content:encoded"]');
    $this->assertEqual((string)$comment_body[0]->p, $comment->comment, "RDFa markup for the comment body found.");
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
