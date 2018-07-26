// TODO: eplace mock

class Records {
  constructor() {
    this.data = [
      {
        id: 1,
        albumName: 'The Last Waltz',
        artists: [
          {
            id: 1,
            name: 'The Band',
            members: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            description: '',
          },
        ],
        releases: [
          {
            recordLabel: 'MGM',
            tracks: [
              { id: 1, title: 'Theme from the Last Waltz', length: '3:28' },
              { id: 2, title: 'Up on Cripple Creek', length: '4:44' },
            ],
            people: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            format: '4xLP',
            releaseDate: '1/1/1970',
            releaseCountry: 'US',
            status: '',
          },
        ],
        description: 'The Last Waltz was a concert by the Canadian-American rock group The Band, held on American Thanksgiving Day, November 25, 1976, at Winterland Ballroom in San Francisco. The Last Waltz was advertised as The Band\'s "farewell concert appearance",[2] and the concert saw The Band joined by more than a dozen special guests, including Eric Clapton, Ringo Starr, Bob Dylan, Ronnie Wood, Muddy Waters, Neil Young, Neil Diamond, Van Morrison, Bobby Charles, Dr. John, Paul Butterfield, Emmylou Harris, Ronnie Hawkins, Joni Mitchell, and The Staple Singers. The musical director for the concert was The Band\'s original record producer, John Simon.',
      },
      {
        id: 2,
        albumName: 'Stage Freight',
        artists: [
          {
            id: 1,
            name: 'The Band',
            members: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            description: '',
          },
        ],
        releases: [
          {
            recordLabel: 'MGM',
            tracks: [
              { id: 1, title: 'Theme from the Last Waltz', length: '3:28' },
              { id: 2, title: 'Up on Cripple Creek', length: '4:44' },
            ],
            people: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            format: '1xLP',
            releaseDate: '1/1/1970',
            releaseCountry: 'US',
            status: '',
          },
        ],
        description: 'Stage Fright is the third studio album by Canadian-American group the Band, released in 1970. It featured two of the group\'s best known songs, "The Shape I\'m In" and "Stage Fright", both of which showcased inspired lead vocal performances (by Richard Manuel and Rick Danko, respectively) and became staples in the group’s live shows.',
      },
      {
        id: 3,
        albumName: 'Music from Big Pink',
        artists: [
          {
            id: 1,
            name: 'The Band',
            members: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            description: '',
          },
        ],
        releases: [
          {
            recordLabel: 'MGM',
            tracks: [
              { id: 1, title: 'Theme from the Last Waltz', length: '3:28' },
              { id: 2, title: 'Up on Cripple Creek', length: '4:44' },
            ],
            people: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            format: '1xLP',
            releaseDate: '1/1/1970',
            releaseCountry: 'US',
            status: '',
          },
        ],
        description: 'Music from Big Pink is the debut studio album by the Band.[1] Released in 1968, it employs a distinctive blend of country, rock, folk, classical, R&B, and soul. The music was composed partly in "Big Pink", a house shared by Rick Danko, Richard Manuel and Garth Hudson in West Saugerties, New York. The album itself was recorded in studios in New York and Los Angeles in 1968,[2] and followed the band\'s backing of Bob Dylan on his 1966 tour (as the Hawks) and time spent together in upstate New York recording material that was officially released in 1975 as The Basement Tapes, also with Dylan. The cover artwork is a painting by Dylan.',
      },
    ];
  }

  all() {
    return this.data;
  }

  get(id) {
    return this.data.find(r => r.id === Number(id));
  }
}

class Artists {
  constructor() {
    this.data = [
      {
        id: 1,
        name: 'The Band',
        members: [
          { id: 1, name: 'Rick Danko' },
          { id: 2, name: 'Levon Helm' },
          { id: 3, name: 'Garth Hudson' },
          { id: 4, name: 'Richard Manual' },
        ],
        description: '',
        discography: [
          {
            id: 1,
            albumName: 'The Last Waltz',
            label: 'MGM',
            releaseDate: '1/1/1970',
          },
        ],
      },
      {
        id: 2,
        name: 'The Grateful Dead',
        members: [
          { id: 5, name: 'Jerry Garcia' },
          { id: 6, name: 'Bob Weir' },
          { id: 7, name: 'Pigpen' },
          { id: 8, name: 'Phil Lesh' },
        ],
        description: '',
        discography: [{}],
      },
    ];
  }

  all() {
    return this.data;
  }

  get(id) {
    return this.data.find(a => a.id === Number(id));
  }
}

class People {
  constructor() {
    this.data = [
      {
        id: 1,
        name: 'Levon Helm',
        description: 'Mark Lavon "Levon" Helm (May 26, 1940 – April 19, 2012)[1] was an American musician and actor who achieved fame as the drummer and one of the vocalists for The Band. Helm was known for his deeply soulful, country-accented voice, multi-instrumental ability, and creative drumming style, highlighted on many of the Band\'s recordings, such as "The Weight", "Up on Cripple Creek", and "The Night They Drove Old Dixie Down".',
        involved: [{}],
      },
    ];
  }

  all() {
    return this.data;
  }

  get(id) {
    return this.data.find(p => p.id === Number(id));
  }
}

const RecordCrateAPI = {
  records: new Records(),
  artists: new Artists(),
  people: new People(),
};

export default RecordCrateAPI;
