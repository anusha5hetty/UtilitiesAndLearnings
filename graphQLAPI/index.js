// Start server using command
// npm run devStart where devStart is the name in the script in package.json
// or
// change the script name to start and then command npm start will start the server

const express = require('express');
const expressGraphQL = require('express-graphql').graphqlHTTP;
const { GraphQLSchema, GraphQLObjectType, GraphQLString, GraphQLList, GraphQLInt, GraphQLNonNull } = require('graphql');

const app = express()

const books = [
    { id: 1, name: "Harry Potter 1", authorId: 1 },
    { id: 2, name: "Harry Potter 2", authorId: 1 },
    { id: 3, name: "Harry Potter 3", authorId: 1 },
    { id: 4, name: "Harry Potter 4", authorId: 1 },
    { id: 5, name: "Harry Potter 5", authorId: 1 },
    { id: 6, name: "Harry Potter 6", authorId: 1 },
    { id: 7, name: "Harry Potter 7", authorId: 1 },
    { id: 8, name: "LOR 1", authorId: 2 },
    { id: 9, name: "LOR 2", authorId: 2 },
    { id: 10, name: "LOR 3", authorId: 2 },
    { id: 11, name: "If Tomorrow Comes", authorId: 3 }
]

const authors = [
    { id: 1, name: "J K Rowling" },
    { id: 2, name: "J R R Tolkien" },
    { id: 3, name: "Sydney Sheldon" }
]


const BookType = new GraphQLObjectType({
    name: 'Book',
    description: "This represents the book",
    // This is a function and not just a object because there is a loop call. BookType is referencing AuthorType and AuthorType is referencing BookType
    fields: () => ({
        // resolve is not required because the data is passed to this through RootQueryType
        id: { type: new GraphQLNonNull(GraphQLInt) },
        name: { type: new GraphQLNonNull(GraphQLString) },
        authorId: { type: new GraphQLNonNull(GraphQLInt) },
        author: {
            type: AuthorType,
            description: "Author Details",
            // resolve takes a function with two optional parameters - parent and args. In the below case we are passing books as parent of the component author
            resolve: (bookAsParent) => {
                return authors.find(author => author.id == bookAsParent.authorId)
            }
        }
    })
})

const AuthorType = new GraphQLObjectType({
    name: 'Author',
    description: "This represents the author",
    fields: {
        id: { type: new GraphQLNonNull(GraphQLInt) },
        name: { type: new GraphQLNonNull(GraphQLString) },
        books: {
            type: new GraphQLList(BookType),
            description: "List of books",
            resolve: (author) => {
                return books.filter(book => author.id == book.authorId)
            }
        }
    }
})

// IF you add paranthesis to the function like this " () => ({}) ", everything within the paranthesis will be returned, in this case the empty object

const RootQueryType = new GraphQLObjectType({
    name: "Query",
    description: "Root Query",
    fields: () => ({
        // To get a single book by filters.
        // Request Payload as below
        // {
        //     book(id: 1) {
        //         name
        //     }
        // }

        book: {
            type: BookType,
            description: "Returns Single Book",
            args: {
                id: { type: GraphQLInt },
                name: { type: GraphQLString }
            },
            resolve: (parent, args) => {
                const val = books.find(book => book.id == args.id || book.name == args.name)
                return val
            }
        },
        books: {
            type: new GraphQLList(BookType),
            description: "List of books",
            resolve: () => books
        },
        authors: {
            type: new GraphQLList(AuthorType),
            description: "List of books",
            resolve: () => authors
        }
    })
})

const schema = new GraphQLSchema({
    query: RootQueryType
})

app.use('/graphql', expressGraphQL({
    schema: schema,
    graphiql: true
}))



app.listen(5000, () => console.log(`[Anusha] Server Up`))