book.title = "Nineteen Eighty-Four"
book.save()
# Confirm update
Book.objects.get(id=book.id)
# Output: <Book: Nineteen Eighty-Four by George Orwell>
